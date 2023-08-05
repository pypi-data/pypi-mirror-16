"""A functional interface for variant calling, postprocessing of and
generating summary statistics for variant call files.

The varcall function implements parallel variant calling using
samtools/bcftools and the multiallelic calling model introduced with samtools
version 1.0.
The varextract function can extract variant sites from BCF input generated with
varcall(), and the function get_coverage_from_vcf can use the same type of
input to generate a coverage report.
"""

import sys
import os
import io
import tempfile
import time
import signal
import random
import subprocess
import locale

from threading import Thread
from collections import OrderedDict, Counter

from . import catch_sigterm, __version__
from . import encoding_base
from . import samheader, pysamtools, tmpfiles, pyvcf, config, pysam, pybcftools, fasta
from . import FormatParseError, SamtoolsRuntimeError

from .encoding_base import DEFAULTENCODING, ExternalApplicationCall


def varcall(ref_genome, inputfiles, output_vcf = None, depth = None, 
            group_by_id = False, md5check = True, threads = None,
            verbose = False, quiet = True):
    """Variant calling using samtools mpileup and bcftools.

    The function speeds up variant calling through multiprocessing
    (currently one instance each of mpileup and bcftools is used per
    chromosome).
    
    Arguments:
    ref_genome: reference genome file (mpileup -f parameter,
                but the funcion will take care of indexing the genome)
    inputfiles: an iterable of inputfiles (the function will take care
                of indexing all of them)
    output_vcf:   optional, name of the variant sites vcf file
                  (default = stdout)
    depth: optional, max per-BAM depth (to avoid excessive memory usage
           (mpileup option -d)
    group_by_id: if True, reads with different read group IDs are never pooled;
                 if False, reads with matching sample names are grouped
                 independent of their read group IDs (samtools' default).
    md5check: if True, the function will compare md5sums between the inputfile
              and the ref_genome sequences and raise an error if it encounters
              any sequences without matching counterparts; the check is skipped
              if md5check is False or if the inputfile headers do not provide
              md5 information for every sequence."""

    tempfile_dir = config.tmpfile_dir
    if not threads:
        threads = config.multithreading_level
    signal.signal(signal.SIGTERM, catch_sigterm)
# ARGUMENTS PREPROCESSING
# additional information via stdout: parameter settings

    if not isinstance(depth, (int, type(None))):
        raise TypeError("Need integer or None value for 'depth' parameter.")

    # retrieve chromosome and read group names from input file headers
    # get all headers and assert that they use the same sequence dictionary
    inputheaders = [samheader.Header.frombam(file) for file in inputfiles]

    # require non-empty and identical sequence dictionaries in the BAM input files
    if any(h['SQ'] == [] for h in inputheaders):
        raise RuntimeError ('Detected a BAM file without sequence dictionary. This does not seem to be an aligned reads file.')
    if not all(h['SQ'] == inputheaders[0]['SQ'] for h in inputheaders[1:]):
        raise RuntimeError ('The input files use different reference sequence dictionaries in their headers. Cannot start combined SNP calling.')

    seqdict = inputheaders[0]['SQ'] # get the chromosome names from the header of the first file
    all_read_groups = [rg for h in inputheaders for rg in h['RG']] # get the read groups of all input files as a flat list
    
    if verbose:
        print ('INPUT FILE SUMMARY:')
        print ()
        print ('Read groups found:')
        for rg in all_read_groups:
            print('ID: {0}\tSample Name: {1}'.format(rg['ID'], rg.get('SM', '-')))
        print ('Sequences found:')
        for seq in seqdict:
            print (seq['SN'])
        print ()
    
    # require sample names for every read group
    if not all(rg.get('SM') for rg in all_read_groups):
        raise RuntimeError('Variant calling requires a sample name specified for every read group. You should reheader your BAM input file(s).')

    # check that all reference genome sequences have vcf compatible titles
    # raise a FormatParseError if incompatible sequence titles are found
    with open(ref_genome, 'r', encoding=fasta.defaultencoding) as ifo:
        fasta.assert_valid_ids(fasta.FastaReader(ifo).identifiers())

    require_reheader = False
    # currently, there are two situations when we need to reheader the input
    # bam files
    # no. 1: the reference genome has sequence names that do not match the bam
    # sequence dictionary; if that's the case, but corresponding sequences can
    # be identified through their MD5 checksums, then we use the reference
    # names.
    # no. 2: if strict grouping (by RG ID) is active but there are duplicate
    # sample names defined in the bam headers, we need to make them unique
    # (by appending the RG ID to them) to prevent samtools from treating these
    # together.

    if md5check:
        # check md5sums of reference and bam header seqs to verify identity of
        # reference during alignment and variant calling
        for seq in seqdict:
            if not seq.get('M5'):
                break
        else:
            # we do this only if every sequence in the first header has an M5 entry
            if verbose:
                print ('md5 checksum comparison between BAM input and reference genome ...', end = ' ')
            with open(ref_genome, 'r', encoding=fasta.defaultencoding) as ifo:
                md5sums = {md5: title
                           for title, md5 in fasta.FastaReader(ifo).md5sums()}
            try:
                for seq in seqdict:
                    if md5sums[seq['M5']] != seq['SN']:
                        # go through all SQs of all headers and replace matching sequence names
                        # with the name found in the reference genome
                        for hdr in inputheaders:
                            for s in hdr['SQ']:
                                if s['SN'] == seq['SN']:
                                    s['SN'] = md5sums[seq['M5']]
                        require_reheader = True
            except KeyError:
                raise RuntimeError("""Non-matching md5sums between reference genome and bam header sequences!
Please use the same reference genome that was used for the alignment to call variants.""")
            if verbose:
                print ('passed',
                       '(some sequences appear to have different names in the BAM input and the reference genome; going to use reference names)' if require_reheader else '')
                print ()
                
    if group_by_id and len(all_read_groups) != len({rg['SM'] for rg in all_read_groups}):
        # grouping of samples should occur strictly by read group ID,
        # but there are duplicate sample names in our input files
        # reheader input files to obtain unique sample names
        require_reheader = True
        if verbose:
            print('Going to reheader the input files to group samples by read group id ...')
        for hdr in inputheaders:
            hdr.uniquify_sm() # change header SM entries to <old_sm>_<rg_id>

    original_files, inputfiles = inputfiles, []
    if verbose:
        print('Preparing input files ...')
    # starting temporary file IO
    tmp_io = [] # will be replaced with the list of temporary files created
    try:
        # inside this block, make sure temporary output files get removed
        try:
            # Temporary input files do not have to be kept around until the end of the analysis,
            # so they are handled by this inner block.
            if require_reheader:
                for hdr, ifile in zip(inputheaders, original_files):
                    tmp_reheadered = []
                    tmp_output = tmpfiles.unique_tmpfile_name('tmpbam_', '.bam')
                    tmp_reheadered.append(tmp_output)
                    if verbose:
                        print ('original file: {0} ---> reheadered copy: {1}'.format(ifile, tmp_output))
                    pysamtools.reheader(hdr, ifile, tmp_output)
                # use the reheadered files as the input files
                inputfiles = tmp_reheadered
                # recalculate the all_read_groups list
                all_read_groups = [rg for h in inputheaders for rg in h['RG']] # a flat list of the read groups from all input files
            else:
                inputfiles = [tmpfiles.tmp_hardlink(ifile, 'tmp_indexed_bam_', '.bam') for ifile in original_files]
                if verbose:
                    for n, b in zip(inputfiles, original_files):
                        print ('Generated hard link {0} from {1}.'.format(n,b))

            # generate a mapping of rg ids to sample names
            rgid_sm_mapping = {rg['ID']:rg['SM'] for rg in all_read_groups} # a dict mapping of all read group IDs to their sample names
            
            # index the reference genome
            tmp_ref_genome = tmpfiles.tmp_hardlink(ref_genome, 'tmp_genome', '.fa')
            if verbose:
                print('Generated hard link {0} for reference genome file {1}.'.format(tmp_ref_genome, ref_genome))
                print()
                print('indexing the reference genome ...', end=' ')
            pysamtools.faidx(tmp_ref_genome)
            if verbose:
                print('done')
                print()
            # index the inputfiles
            if verbose:
                print ('indexing the aligned reads input files ...', end=' ')
                sys.stdout.flush()
            for file in inputfiles:
                pysamtools.index(file)
            if verbose:
                print ('done')
                print ()

            # Create a tuple of calls to samtools mpileup and bcftools for each contig.
            # The contig name is stored as the third element of that tuple.
            calls = [(
                [config.samtools_exe, 'mpileup', '-d', str(depth) if depth else '',
                 '-r', seq['SN'] + ':', '-t', 'DP,DPR', '-gu', '-f', tmp_ref_genome]
                + inputfiles,
                [config.bcftools_exe, 'call',  '-m', '-A', '-f', 'GQ', '-O', 'b', '-'],
                seq['SN']
                ) for seq in seqdict]

            if verbose:
                print ('Starting variant calling ..')

            # create and open temporary output files with unique names
            # to redirect subprocess output to
            # generate files with readable and file system-compatible names
            prefixes = [''.join(c if c.isalnum() else '_' for c in seq['SN']) for seq in seqdict]
            tmp_io = [tempfile.NamedTemporaryFile(mode='wb',
                                                  prefix=p + '_',
                                                  suffix='.bcf',
                                                  dir=config.tmpfile_dir,
                                                  delete=False)
                      for p in prefixes]

            # launch subprocesses and monitor their status
            subprocesses = []
            error_table = {}
            def enqueue_output(out, stderr_buffer):
                for line in iter(out.readline, b''):
                    # Eventually we are going to print the contents of
                    # the stderr_buffer to sys.stderr so we can
                    # decode things here using its encoding.
                    # We do a 'backslashreplace' just to be on the safe side.
                    stderr_buffer.write(line.decode(sys.stderr.encoding,
                                                    'backslashreplace'))
                out.close()
                
            try:
                while subprocesses or calls:
                    while calls and len(subprocesses) < threads:
                        # launch a new combined call to samtools mpileup and bcftools 
                        call = calls.pop()
                        c_str = (' '.join(call[0]), ' '.join(call[1]))
                        contig = call[2]
                        error_table[c_str] = [io.StringIO(), io.StringIO()]
                        ofo = tmp_io[len(calls)] # calls and temporary output file objects have the same order

                        p1 = subprocess.Popen(call[0], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                        p2 = subprocess.Popen(call[1], stdin = p1.stdout, stdout = ofo, stderr = subprocess.PIPE)
                        p1.stdout.close()
                        t1 = Thread(target = enqueue_output, args=(p1.stderr, error_table[c_str][0]))
                        t2 = Thread(target = enqueue_output, args=(p2.stderr, error_table[c_str][1]))
                        t1.daemon = t2.daemon = True
                        t1.start()
                        t2.start()
                        subprocesses.append((c_str, p1, p2, contig))
                        
                        if verbose:
                            print ('Calling variants for contig: {0}'.format(call[2]))
                            
                    for call, p1, p2, contig in subprocesses:
                        # monitor processes
                        p1_stat = p1.poll()
                        p2_stat = p2.poll()
                        if p1_stat is not None or p2_stat is not None:
                            # there is an outcome for this process, lets see what it is
                            if p1_stat or p2_stat:
                                print()
                                print(error_table[call][0].getvalue(), error_table[call][1].getvalue(),
                                      file = sys.stderr)
                                raise SamtoolsRuntimeError(
                                    'Variant Calling for contig {0} failed.'.format(contig),
                                    call = '{0} | {1}'.format(call[0], call[1])
                                    )
                            if p2_stat == 0:
                                # things went fine
                                if verbose:
                                    print()
                                    print('Contig {0} finished.'.format(contig))
                                if not quiet:
                                    print()
                                    print('stderr output from samtools mpileup/bcftools:'.upper(), file = sys.stderr)
                                    print(error_table[call][0].getvalue(), error_table[call][1].getvalue(),
                                       file = sys.stderr)
                                del error_table[call]
                                subprocesses.remove((call, p1, p2, contig))
                                break
                    # wait a bit in between monitoring cycles
                    time.sleep(2)
            finally:
                for call, p1, p2, contig in subprocesses:
                    # make sure we do not leave running subprocesses behind
                    for proc in (p1, p2):
                        try:
                            proc.terminate()
                        except:
                            pass
                for tmp_file in tmp_io:
                    tmp_file.close()
        finally:
            try:
                # Make sure remaining buffered stderr output of mpileup/bcftools
                # does not get lost.
                # mpileup and bcftools write a lot to stderr.
                # Currently, we don't screen this output for real errors,
                # but simply rewrite everything.
                if not quiet and error_table:
                    print()
                    print('stderr output from samtools mpileup/bcftools:'.upper(), file = sys.stderr)
                    for call, errors in error_table.items():
                        print (' | '.join(call), ':', file = sys.stderr)
                        print ('-' * 20, file = sys.stderr)
                        print ('samtools mpileup output:', file = sys.stderr)
                        print (errors[0].getvalue(), file = sys.stderr)
                        print ('bcftools view output:', file = sys.stderr)
                        print (errors[1].getvalue(), file = sys.stderr)
            except:
                pass
            # Remove temporary input files.
            # Further work involves only the temporary per-contig output files
            # that were just written.
            for tmp_bam in inputfiles:
                # when we get here, the original input files are tucked away
                # in original_files, so if inputfiles has any elements, these
                # are guaranteed to be temporary file names
                try:
                    os.remove(tmp_bam)
                except:
                    pass
                try:
                    os.remove(tmp_bam + '.bai')
                except:
                    pass
            try:
                os.remove(tmp_ref_genome)   # hard link to reference genome
            except:
                pass
            try:
                os.remove(tmp_ref_genome + '.fai')  # indexed reference genome
            except:
                pass

        #************************* call to bcftools concat *******************
        if verbose:
            print()
            print('Writing final variant calls ...', end=' ')
            sys.stdout.flush()
        # obtain a pybcftools.bcfHeader representation of the first file's header
        bcf_header = pybcftools.get_header(tmp_io[0].name)
        # generate a vcf representation to modify
        template_header = pyvcf.VCFReader(bcf_header).info
        # TO DO: The following header modification code block
        # should be refactored into a separate function,
        # preferably inside the pyvcf module.
        # remove all samtools/bcftools-specific comment lines from header
        # add tool-specific header lines
        comments_to_remove = [comment for comment in template_header.meta if comment.startswith('samtools') or comment.startswith('bcftools')]
        for comment in comments_to_remove:
            del template_header.meta[comment]
        template_header.meta['reference'] = [ref_genome]
        template_header.meta['source'] = ['MiModD varcall (version {0})'.format(__version__)]
        template_header.meta['MiModDCommand'] = ['mimodd ' + ' '.join(sys.argv[1:])]
        template_header.meta['samtoolsCommand'] = ['n.a. (wrapped by MiModD)']
        template_header.meta['bcftools_callCommand'] = ['n.a. (wrapped by MiModD)']
        if all_read_groups:
            template_header.meta['rginfo'] = OrderedDict()
        for rg_no, rg in enumerate(all_read_groups):
            # Each rginfo element gets a numeric ID value.
            # This is different from the SAM/BAM RG ID, which is stored
            # separately under a Rgid key
            rginfo_id = str(rg_no)
            template_header.meta['rginfo'][rginfo_id] = OrderedDict()
            template_header.meta['rginfo'][rginfo_id]['Rgid'] = pyvcf.EscapedMetaString(rg['ID'])
            if rg.get('SM'):
                template_header.meta['rginfo'][rginfo_id]['Name'] = pyvcf.EscapedMetaString(rg['SM'])
            if rg.get('DS'):
                template_header.meta['rginfo'][rginfo_id]['Description'] = pyvcf.EscapedMetaString(rg['DS'])
        # update the bcfHeader representation with the modified content
        bcf_header.lines = template_header.getlines()
        
        try:
            # write the modified bcf representation to a temporary file
            bcf_hdr_file = tempfile.NamedTemporaryFile(mode = 'wb', suffix = '.bcf', prefix = 'header',
                                            dir = config.tmpfile_dir, delete = False)
            bcf_hdr_file.write(bytes(bcf_header))
            bcf_hdr_file.close()
            # concatenate the temporary header file and all original bcf files
            call_args = ['-o', output_vcf, '-O', 'b', bcf_hdr_file.name]
            call_args += [f.name for f in tmp_io]
            proc = ExternalApplicationCall(command=config.bcftools_exe,
                                           subcommand='concat',
                                           args=call_args,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
            ret = proc.run()
            if proc.run_info.errors:
                if verbose:
                    print()
                raise SamtoolsRuntimeError('Failed to merge temporary files.',
                                           proc.run_info.call, proc.run_info.errors)
            if verbose:
                print ('done')
                print ()
                print ('Variant Calling finished.')
        finally:
            try:
                os.remove(bcf_hdr_file.name)
            except:
                pass
    finally:
        # remove temporary per-contig output files
        for file in tmp_io:
            try:
                os.remove(file.name)
            except:
                pass

        
def varextract (inputfile, output_vcf = None, vcf_pre = None,
                keep_alts = False, verbose = False):
    """
    vcf_pre: optional list of pre-existing vcf files to be included in the variant calling."""
    
    # open all necessary input and output files
    # read the vcf specified by sites
    if output_vcf:
        out_vcf = open(output_vcf, 'w', encoding=pyvcf.defaultencoding)
    else:
        out_vcf = encoding_base.get_custom_std(sys.stdout,
                                               encoding=pyvcf.defaultencoding)

    try:
        sites = {}
        site_sample_names = []
        if vcf_pre:
            for file_no, filename in enumerate(vcf_pre):
                with pyvcf.open(filename, 'r') as current_vcf:
                    samples = OrderedDict(
                        [('external_source_{0}{1}'
                          .format(file_no+1, '_' + name if name else ''), info)
                         for name, info in current_vcf.info.samples.items()
                         ])
                    site_sample_names.append(samples)
                    for record in current_vcf:
                        if not 'INDEL' in record.info:
                            sites.setdefault((record.chrom, record.pos), []).append((file_no, record.alt_list, record.sampleinfo)) # fast lookup!

        # pyvcf.open returns a VCFReader object for convenient access to a vcf file
        with pyvcf.open(inputfile, 'rb') as raw_vcf:
            # copy comment and header lines over to post-processed vcf file
            # determine the number of samples and their names from the vcf input
            samples = raw_vcf.info.samples   # retrieve the sample names from the VCFReader object
            sample_count = len(samples)
            extended_samples = OrderedDict()
            extended_samples.update(samples)
            for names in site_sample_names:
                extended_samples.update(names)
            raw_vcf.info.samples = extended_samples
            # write the headers to the output files
            out_vcf.write(str(raw_vcf.info)+'\n')
            raw_vcf.info.samples = samples
            
            # start writing the real content
            for line in raw_vcf.raw_iter():    # the raw_iter() method of the VCFReader object provides fast, line-based access to the body of a vcf file
                fields = line.split()
                chrom = fields[0]
                pos = int(fields[1])

                try:
                    if (chrom, pos) in sites:
                        var = pyvcf.VCFEntry(line, samples)
                        pre_info = sites[(chrom, pos)]
                        var.samplenames = tuple(extended_samples)
                        sample_keys = [key for key in var.sampleinfo.keys() if key != 'GT']
                        for names in site_sample_names:
                            for name in names:
                                for key in sample_keys:
                                    var.sampleinfo[key][name] = '.'
                        
                        for file_no, current_record_alt, ori_record_sampleinfo in pre_info:
                            # ori_record_sampleinfo is an OrderedDict
                            # containing dicts as values.
                            # We need to make a time-consuming deep copy of this structure
                            # because otherwise we will change sites[(chrom, pos)] directly,
                            # when we might encounter the same chrom, pos tuple again in
                            # the same vcf (when e.g. a site has evidence for an INDEL) and
                            # might need the original information again.
                            # In compensation, we do not need order preserved in the
                            # following code so we can use a regular dict for the copy.
                            current_record_sampleinfo = {}
                            for key, value in ori_record_sampleinfo.items():
                                current_record_sampleinfo[key] = value.copy()
                            if 'GT' not in current_record_sampleinfo:
                                current_record_sampleinfo['GT'] = {}
                                # initialize all missing GT fields to 1/1 = homozygous mutant
                                # if there is at least one ALT allele
                                # to 0/0 = homozygous wt otherwise
                                if current_record_alt:
                                    gen_ini = '1/1'
                                else:
                                    gen_ini = '0/0'
                                for name in site_sample_names[file_no]:
                                    current_record_sampleinfo['GT'][name] = gen_ini
                            if not var.alt:
                                # just use pre_info's alternate alleles and
                                # update the original samples' DPR field to reflect the new number of alleles
                                for name in samples:
                                    assert var.sampleinfo['DP'][name] == var.sampleinfo['DPR'][name], line
                                    var.sampleinfo['DPR'][name] = var.sampleinfo['DPR'][name] + ',0'*len(current_record_alt)
                                var.alt_list = current_record_alt
                            else:
                                # merge pre_info's alternate alleles with existing ones,
                                # update the original samples' DPR field to reflect the new number of alleles
                                old_allelelist = var.alt_list
                                var.alt_list = var.alt_list + current_record_alt
                                for name in samples:
                                    var.sampleinfo['DPR'][name] = var.sampleinfo['DPR'][name] + ',0'*(len(var.alt_list)-len(old_allelelist))
                                
                                # adjust pre_info's 'GT' information, if present, to reflect the new order of variant alleles
                                allele_no_mapping = {'.' : '.',
                                                     '0' : '0'}
                                new_allelelist = var.alt_list # var.alt_list is a property so storing the value once makes things faster
                                for old_allele_no, allele in enumerate(current_record_alt, 1):
                                    allele_no_mapping[str(old_allele_no)] = str(new_allelelist.index(allele)+1)
                                for name in site_sample_names[file_no]:
                                    current_record_sampleinfo['GT'][name] = '/'.join(
                                            allele_no_mapping[allele_no] for allele_no in
                                            current_record_sampleinfo['GT'][name].split('/'))

                            # update the GT fields of the current variant
                            for name in site_sample_names[file_no]:
                                var.sampleinfo['GT'][name] = current_record_sampleinfo['GT'][name]
                                # all other fields are currently ignored
                                # for key in sample_keys:
                                #    if key in current_record_sampleinfo:
                                #        var.sampleinfo[key][name] = current_record_sampleinfo[key][name]
                           
                        out_vcf.write(str(var)+'\n')
                    elif fields[4] != '.':
                        # this is an original variant site
                        # with no information in the supplied vcfs
                        # => fill the vcf columns with default values
                        var = pyvcf.VCFEntry(line, samples)
                        if keep_alts or any(allele_no != '.' and allele_no != '0' for gt in var.sampleinfo['GT'].values() for allele_no in gt.split('/')):
                            var.samplenames = tuple(extended_samples)
                            sample_keys = var.sampleinfo.keys()
                            for names in site_sample_names:
                                for name in names:
                                    for key in sample_keys:
                                        var.sampleinfo[key][name] = '.'
                                    var.sampleinfo['GT'][name] = './.'
                            out_vcf.write(str(var)+'\n')
                except:
                    raise RuntimeError(line)

    # clean up
    finally:
        if out_vcf is not sys.stdout:
            try:
                out_vcf.close()
            except:
                pass


def get_coverage_from_vcf (inputfile, ofile = None):
    if ofile:
        out_stats = open(ofile, 'w', encoding=DEFAULTENCODING)
    else:
        out_stats = encoding_base.get_custom_std(sys.stdout)
    try:
        with pyvcf.open(inputfile, 'rb') as raw_vcf:
            # write header line
            out_stats.write('#CHROM\t{0}\n'
                            .format('\t'.join([sample
                                               for sample in
                                               raw_vcf.info.samples]))
                            )
            # start coverage calculation over input
            cov_dist = get_per_sample_field_dist(raw_vcf, 'DP')
            # cov_dist is a rather complex structure,
            # which we now simplify to an OrderedDict, in which the keys
            # are contig names and each value is a list of sample-specific
            # mean coverage values
            summary = OrderedDict()
            for chrom, per_sample_dists in cov_dist.items():
                sites = sum(per_sample_dists[0].values())
                summary[chrom] = [sum(int(coverage) * freq
                                      for coverage, freq in dist.items())
                                  // sites
                                  for dist in per_sample_dists]
            # write results
            for chrom, mean_covs in summary.items():
                out_stats.write(chrom)
                out_stats.write('\t')
                out_stats.write('\t'.join(str(mean) for mean in mean_covs))
                out_stats.write('\n')
    finally:
        if out_stats is not sys.stdout:
            try:
                out_stats.close()
            except:
                pass


def get_per_sample_field_dist (ivcf, field):
    """Get per-sample distributions of the values in a sample-specific field.

    Returns an OrderedDict, in which the keys are contig names and the values
    are lists of Counters (one per sample) of the field values.
    All field values are stored as strings."""
    
    dist = OrderedDict()
    for field_info in ivcf.field_iter(field):
        try:
            contig_dist = dist[field_info[0]]
        except KeyError:
            dist[field_info[0]] = [Counter()
                                   for sample in ivcf.info.samples]
            contig_dist = dist[field_info[0]]
        for i, value in enumerate(field_info[2]):
            contig_dist[i][value] += 1
    return dist
