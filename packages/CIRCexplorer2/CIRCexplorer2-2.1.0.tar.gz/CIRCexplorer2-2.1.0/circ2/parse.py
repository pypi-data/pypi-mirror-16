"""
Usage: CIRCexplorer2 parse [options] -t ALIGNER <fusion>

Options:
    -h --help                      Show help message.
    --version                      Show version.
    -t ALIGNER                     Aligner (TopHat-Fusion, STAR, MapSplice, \
BWA, segemehl).
    -o OUT --output=OUT            Output directory. [default: circ_out]
"""

import sys
import os.path
import pysam
from collections import defaultdict
from dir_func import create_dir
from helper import logger
from parser import parse_fusion_bam, Cigar

__author__ = 'Xiao-Ou Zhang (zhangxiaoou@picb.ac.cn)'

__all__ = ['parse']


@logger
def parse(options):
    aliger = set(['TopHat-Fusion', 'STAR', 'MapSplice', 'BWA', 'segemehl'])
    if options['-t'] not in aliger:
        sys.exit('Error: CIRCexplorer2 parse does not support %s!' %
                 options['-t'])
    # check output directory
    create_dir(options['--output'])
    out_dir = os.path.abspath(options['--output'])
    out = out_dir + '/fusion_junction.bed'
    # parse fusion junctions from other aligers
    if options['-t'] == 'TopHat-Fusion':
        tophat_fusion_parse(options['<fusion>'], out)
    elif options['-t'] == 'STAR':
        star_parse(options['<fusion>'], out)
    elif options['-t'] == 'MapSplice':
        mapsplice_parse(options['<fusion>'], out)
    elif options['-t'] == 'BWA':
        bwa_parse(options['<fusion>'], out)
    elif options['-t'] == 'segemehl':
        segemehl_parse(options['<fusion>'], out)


def tophat_fusion_parse(fusion, out):
    '''
    Parse fusion junctions from TopHat-Fusion aligner
    '''
    print('Start parsing fusion junctions from TopHat-Fusion...')
    fusions = defaultdict(int)
    for i, read in enumerate(parse_fusion_bam(fusion)):
        chrom, strand, start, end = read
        segments = [start, end]
        if (i + 1) % 2 == 1:  # first fragment of fusion junction read
            interval = [start, end]
        else:  # second fragment of fusion junction read
            sta1, end1 = interval
            sta2, end2 = segments
            if end1 < sta2 or end2 < sta1:  # no overlap between fragments
                sta = sta1 if sta1 < sta2 else sta2
                end = end1 if end1 > end2 else end2
                fusions['%s\t%d\t%d' % (chrom, sta, end)] += 1
    total = 0
    with open(out, 'w') as outf:
        for i, pos in enumerate(fusions):
            outf.write('%s\tFUSIONJUNC_%d/%d\t0\t+\n' % (pos, i, fusions[pos]))
            total += fusions[pos]
    print('Converted %d fusion reads!' % total)


def star_parse(fusion, out):
    '''
    Parse fusion junctions from STAR aligner
    '''
    print('Start parsing fusion junctions from STAR...')
    junc = defaultdict(int)
    with open(fusion, 'r') as junc_f:
        for line in junc_f:
            flag = int(line.split()[6])
            if flag < 0:
                continue
            chr1, site1, strand1, chr2, site2, strand2 = line.split()[:6]
            if chr1 != chr2 or strand1 != strand2:
                continue
            if strand1 == '+':
                start = int(site2)
                end = int(site1) - 1
            else:
                start = int(site1)
                end = int(site2) - 1
            if start > end:
                continue
            junc_id = '%s\t%d\t%d' % (chr1, start, end)
            junc[junc_id] += 1
    total = 0
    with open(out, 'w') as outf:
        for i, j in enumerate(junc):
            outf.write('%s\tFUSIONJUNC_%d/%d\t0\t+\n' % (j, i, junc[j]))
            total += junc[j]
    print('Converted %d fusion reads!' % total)


def mapsplice_parse(fusion, out):
    '''
    Parse fusion junctions from MapSplice aligner
    '''
    print('Start parsing fusion junctions from MapSplice...')
    total = 0
    with open(fusion, 'r') as junc_f, open(out, 'w') as outf:
        for i, line in enumerate(junc_f):
            chrom, site1, site2, name, reads, strand = line.split()[:6]
            chr1, chr2 = chrom.split('~')
            if chr1 != chr2:
                continue
            site1 = int(site1)
            site2 = int(site2)
            if strand == '++' and site1 > site2:
                start = site2 - 1
                end = site1
            elif strand == '--' and site1 < site2:
                start = site1 - 1
                end = site2
            else:
                continue
            outf.write('%s\t%d\t%d\tFUSIONJUNC_%d/%s\t0\t+\n' % (chr1, start,
                                                                 end, i,
                                                                 reads))
            total += int(reads)
    print('Converted %d fusion reads!' % total)


def bwa_parse(fusion, out):
    '''
    Parse fusion junctions from BWA aligner
    Origin source codes: Xu-Kai Ma (maxukai@picb.ac.cn)
    Modified: Xiao-Ou Zhang (zhangxiaoou@picb.ac.cn)
    '''
    print('Start parsing fusion junctions from BWA...')
    fusions = defaultdict(int)
    samFile = pysam.AlignmentFile(fusion, 'r')
    for read in samFile:
        if read.is_unmapped:  # unmapped reads
            continue
        if read.is_supplementary:  # supplementary reads
            continue
        if not read.has_tag('SA'):  # no SA tag
            continue
        saInfo = read.get_tag('SA').split(';')[:-1]
        if len(saInfo) >= 2:  # have many supplementary sequence
            continue
        saInfo = saInfo[0].split(',')  # rname,pos,strand,CIGAR,mapQ,NM;
        chr1 = samFile.get_reference_name(read.reference_id)
        chr2 = saInfo[0]
        if chr1 != chr2:  # not same chromosome
            continue
        strand1 = '+' if not read.is_reverse else '-'
        strand2 = saInfo[2]
        if strand1 != strand2:  # not same strand
            continue
        cigar1 = Cigar(read.cigarstring)
        cigar2 = Cigar(saInfo[3])
        pos1 = read.reference_start   # 0-base
        pos2 = int(saInfo[1]) - 1  # 0-base
        if cigar1.is_MS:  # cigars1: M..S
            if not cigar2.is_SM:  # cigar2: not S..M
                continue
            if pos1 <= pos2:  # may be linear junction
                continue
            right = read.reference_end
            unMap1 = read.query_length - cigar1.read_match_len
            map2 = cigar2.read_match_len
            redundence = map2 - unMap1
            left = pos2 + redundence
        elif cigar1.is_SM:  # cigars1: S..M
            if not cigar2.is_MS:  # cigar2: not M..S
                continue
            if pos1 >= pos2:  # may be linear junction
                continue
            left = pos1
            unMap1 = read.query_length - cigar1.read_match_len
            map2 = cigar2.read_match_len
            redundence = map2 - unMap1
            right = pos2 + cigar2.ref_match_len - redundence
        else:
            continue  # not junction for circRNA
        fusions['%s\t%d\t%d' % (chr1, left, right)] += 1
    samFile.close()
    total = 0
    with open(out, 'w') as outF:
        for i, pos in enumerate(fusions):
            outF.write('%s\tFUSIONJUNC_%d/%d\t0\t+\n' % (pos, i, fusions[pos]))
            total += fusions[pos]
    print('Converted %d fusion reads!' % total)


def segemehl_parse(fusion, out):
    '''
    Parse fusion junctions from segemehl aligner
    '''
    print('Start parsing fusion junctions from segemehl...')
    total = 0
    with open(fusion, 'r') as junc_f, open(out, 'w') as outf:
        for i, line in enumerate(junc_f):
            chrom, start, end, info = line.split()[:4]
            if not info.endswith('C:P'):
                continue
            reads = info.split(':')[1]
            start = str(int(start) - 1)
            outf.write('\t'.join([chrom, start, end,
                                  'FUSIONJUNC_%d/%s\t+\n' % (i, reads)]))
            total += int(reads)
    print('Converted %d fusion reads!' % total)
