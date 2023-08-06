#!/usr/bin/env python3
"""
Create tab-delimited database file to store sequence alignment information
"""
# Info
__author__ = 'Namita Gupta, Jason Anthony Vander Heiden'
from changeo import __version__, __date__

# Imports
import csv
import os
import re
import sys
import pandas as pd
import tarfile
import zipfile
from argparse import ArgumentParser
from collections import OrderedDict
from itertools import groupby
from shutil import rmtree
from tempfile import mkdtemp
from textwrap import dedent
from time import time
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Presto and changeo imports
from presto.Defaults import default_out_args
from presto.Annotation import parseAnnotation
from presto.IO import countSeqFile, printLog, printProgress
from changeo.Commandline import CommonHelpFormatter, getCommonArgParser, parseCommonArgs
from changeo.IO import getDbWriter, countDbFile, getRepo
from changeo.Receptor import IgRecord, parseAllele, v_allele_regex, d_allele_regex, \
                             j_allele_regex

# Default parameters
default_delimiter = ('\t', ',', '-')


def gapV(ig_dict, repo_dict):
    """
    Insert gaps into V region and update alignment information

    Arguments:
      ig_dict : Dictionary of parsed IgBlast output
      repo_dict : Dictionary of IMGT gapped germline sequences

    Returns:
      dict : Updated with SEQUENCE_IMGT, V_GERM_START_IMGT, and V_GERM_LENGTH_IMGT fields
    """

    seq_imgt = '.' * (int(ig_dict['V_GERM_START_VDJ']) - 1) + ig_dict['SEQUENCE_VDJ']

    # Find gapped germline V segment
    vgene = parseAllele(ig_dict['V_CALL'], v_allele_regex, 'first')
    vkey = (vgene, )
    #TODO: Figure out else case
    if vkey in repo_dict:
        vgap = repo_dict[vkey]
        # Iterate over gaps in the germline segment
        gaps = re.finditer(r'\.', vgap)
        gapcount = int(ig_dict['V_GERM_START_VDJ']) - 1
        for gap in gaps:
            i = gap.start()
            # Break if gap begins after V region
            if i >= ig_dict['V_GERM_LENGTH_VDJ'] + gapcount:
                break
            # Insert gap into IMGT sequence
            seq_imgt = seq_imgt[:i] + '.' + seq_imgt[i:]
            # Update gap counter
            gapcount += 1
        ig_dict['SEQUENCE_IMGT'] = seq_imgt
        # Update IMGT positioning information for V
        ig_dict['V_GERM_START_IMGT'] = 1
        ig_dict['V_GERM_LENGTH_IMGT'] = ig_dict['V_GERM_LENGTH_VDJ'] + gapcount

    return ig_dict


def getIMGTJunc(ig_dict, repo_dict):
    """
    Identify junction region by IMGT definition

    Arguments:
      ig_dict : Dictionary of parsed IgBlast output
      repo_dict : Dictionary of IMGT gapped germline sequences

    Returns:
      dict : Updated with JUNCTION_LENGTH_IMGT and JUNCTION_IMGT fields
    """
    # Find germline J segment
    jgene = parseAllele(ig_dict['J_CALL'], j_allele_regex, 'first')
    jkey = (jgene, )
    #TODO: Figure out else case
    if jkey in repo_dict:
        # Get germline J sequence
        jgerm = repo_dict[jkey]
        jgerm = jgerm[:ig_dict['J_GERM_START']+ig_dict['J_GERM_LENGTH']-1]
        # Look for (F|W)GXG aa motif in nt sequence
        motif = re.search(r'T(TT|TC|GG)GG[ACGT]{4}GG[AGCT]', jgerm)
        aa_end = len(ig_dict['SEQUENCE_IMGT'])
        #TODO: Figure out else case
        if motif:
            # print('\n', motif.group())
            aa_end = motif.start() - len(jgerm) + 3
        # Add fields to dict
        ig_dict['JUNCTION'] = ig_dict['SEQUENCE_IMGT'][309:aa_end]
        ig_dict['JUNCTION_LENGTH'] = len(ig_dict['JUNCTION'])

    return ig_dict


def getRegions(ig_dict):
    """
    Identify FWR and CDR regions by IMGT definition

    Arguments:
      ig_dict : Dictionary of parsed alignment output

    Returns:
      dict : Updated with FWR1_IMGT, FWR2_IMGT, FWR3_IMGT, FWR4_IMGT,
             CDR1_IMGT, CDR2_IMGT, and CDR3_IMGT fields
    """
    try:
        seq_len = len(ig_dict['SEQUENCE_IMGT'])
        ig_dict['FWR1_IMGT'] = ig_dict['SEQUENCE_IMGT'][0:min(78,seq_len)]
    except (KeyError, IndexError):
        return ig_dict

    try: ig_dict['CDR1_IMGT'] = ig_dict['SEQUENCE_IMGT'][78:min(114, seq_len)]
    except (IndexError): return ig_dict

    try: ig_dict['FWR2_IMGT'] = ig_dict['SEQUENCE_IMGT'][114:min(165, seq_len)]
    except (IndexError): return ig_dict

    try: ig_dict['CDR2_IMGT'] = ig_dict['SEQUENCE_IMGT'][165:min(195, seq_len)]
    except (IndexError): return ig_dict

    try: ig_dict['FWR3_IMGT'] = ig_dict['SEQUENCE_IMGT'][195:min(312, seq_len)]
    except (IndexError): return ig_dict

    try:
        cdr3_end = 306 + ig_dict['JUNCTION_LENGTH']
        ig_dict['CDR3_IMGT'] = ig_dict['SEQUENCE_IMGT'][312:cdr3_end]
        ig_dict['FWR4_IMGT'] = ig_dict['SEQUENCE_IMGT'][cdr3_end:]
    except (KeyError, IndexError):
        return ig_dict

    return ig_dict


def getInputSeq(seq_file):
    """
    Fetch input sequences for IgBlast or iHMMune-align queries

    Arguments:
    seq_file = a fasta file of sequences input to IgBlast or iHMMune-align

    Returns:
    a dictionary of {ID:Seq}
    """

    seq_dict = SeqIO.index(seq_file, "fasta", IUPAC.ambiguous_dna)

    # Create a seq_dict ID translation using IDs truncate up to space or 50 chars
    seqs = {}
    for seq in seq_dict.values():
        seqs.update({seq.description:str(seq.seq)})

    return seqs


def findLine(handle, query):
    """
    Finds line with query string in file

    Arguments:
    handle = file handle in which to search for line
    query = query string for which to search in file

    Returns:
    line from handle in which query string was found
    """
    for line in handle:
        if(re.match(query, line)):
            return line


def extractIMGT(imgt_output):
    """
    Extract necessary files from IMGT results, zipped or unzipped
    
    Arguments:
    imgt_output = zipped file or unzipped folder output by IMGT
    
    Returns:
    sorted list of filenames from which information will be read
    """
    #file_ext = os.path.splitext(imgt_output)[1].lower()
    imgt_flags = ('1_Summary', '2_IMGT-gapped', '3_Nt-sequences', '6_Junction')
    temp_dir = mkdtemp()
    if zipfile.is_zipfile(imgt_output):
        # Open zip file
        imgt_zip = zipfile.ZipFile(imgt_output, 'r')
        # Extract required files
        imgt_files = sorted([n for n in imgt_zip.namelist() \
                             if os.path.basename(n).startswith(imgt_flags)])
        imgt_zip.extractall(temp_dir, imgt_files)
        # Define file list
        imgt_files = [os.path.join(temp_dir, f) for f in imgt_files]
    elif os.path.isdir(imgt_output):
        # Find required files in folder
        folder_files = []
        for root, dirs, files in os.walk(imgt_output):
            folder_files.extend([os.path.join(os.path.abspath(root), f) for f in files])
        # Define file list
        imgt_files = sorted([n for n in folder_files \
                             if os.path.basename(n).startswith(imgt_flags)])
    elif tarfile.is_tarfile(imgt_output):
        # Open zip file
        imgt_tar = tarfile.open(imgt_output, 'r')
        # Extract required files
        imgt_files = sorted([n for n in imgt_tar.getnames() \
                             if os.path.basename(n).startswith(imgt_flags)])
        imgt_tar.extractall(temp_dir, [imgt_tar.getmember(n) for n in imgt_files])
        # Define file list
        imgt_files = [os.path.join(temp_dir, f) for f in imgt_files]
    else:
        sys.exit('ERROR: Unsupported IGMT output file. Must be either a zipped file (.zip), LZMA compressed tarfile (.txz) or a folder.')
    
    if len(imgt_files) > len(imgt_flags): # e.g. multiple 1_Summary files
        sys.exit('ERROR: Wrong files in IMGT output %s.' % imgt_output)
    elif len(imgt_files) < len(imgt_flags):
        sys.exit('ERROR: Missing necessary file IMGT output %s.' % imgt_output)
        
    return temp_dir, imgt_files


# TODO: return a dictionary with keys determined by the comment strings in the blocks, thus avoiding problems with missing blocks
def readOneIgBlastResult(block):
    """
    Parse a single IgBLAST query result

    Arguments:
    block =  itertools groupby object of single result

    Returns:
    None if no results, otherwise list of DataFrames for each result block
    """
    results = list()
    i = 0
    for match, subblock in groupby(block, lambda l: l=='\n'):
        if not match:
            # Strip whitespace and comments
            sub = [s.strip() for s in subblock if not s.startswith('#')]

            # Continue on empty block
            if not sub:  continue
            else:  i += 1

            # Split by tabs
            sub = [s.split('\t') for s in sub]

            # Append list for "V-(D)-J rearrangement summary" (i == 1)
            # And "V-(D)-J junction details" (i == 2)
            # Otherwise append DataFrame of subblock
            if i == 1 or i == 2:
                results.append(sub[0])
            else:
                df = pd.DataFrame(sub)
                if not df.empty: results.append(df)

    return results if results else None


# TODO:  needs more speeds. pandas is probably to blame.
def readIgBlast(igblast_output, seq_dict, repo_dict,
                score_fields=False, region_fields=False):
    """
    Reads IgBlast output

    Arguments:
    igblast_output = IgBlast output file (format 7)
    seq_dict = a dictionary of {ID:Seq} from input fasta file
    repo_dict = dictionary of IMGT gapped germline sequences
    score_fields = if True parse alignment scores
    region_fields = if True add FWR and CDR region fields

    Returns:
    a generator of dictionaries containing alignment data
    """

    # Open IgBlast output file
    with open(igblast_output) as f:
        # Iterate over individual results (separated by # IGBLASTN)
        for k1, block in groupby(f, lambda x: re.match('# IGBLASTN', x)):
            block = list(block)
            if not k1:
                # TODO: move query name extraction into block parser readOneIgBlastResult().
                # Extract sequence ID
                query_name = ' '.join(block[0].strip().split(' ')[2:])
                # Initialize db_gen to have ID and input sequence
                db_gen = {'SEQUENCE_ID':     query_name,
                          'SEQUENCE_INPUT':  seq_dict[query_name]}

                # Parse further sub-blocks
                block_list = readOneIgBlastResult(block)

                # TODO: this is indented pretty far.  should be a separate function. or several functions.
                # If results exist, parse further to obtain full db_gen
                if block_list is not None:
                    # Parse quality information
                    db_gen['STOP'] = 'T' if block_list[0][-4] == 'Yes' else 'F'
                    db_gen['IN_FRAME'] = 'T' if block_list[0][-3] == 'In-frame' else 'F'
                    db_gen['FUNCTIONAL'] = 'T' if block_list[0][-2] == 'Yes' else 'F'
                    if block_list[0][-1] == '-':
                        db_gen['SEQUENCE_INPUT'] = str(Seq(db_gen['SEQUENCE_INPUT'],
                                                           IUPAC.ambiguous_dna).reverse_complement())

                    # Parse V, D, and J calls
                    call_str = ' '.join(block_list[0])
                    v_call = parseAllele(call_str, v_allele_regex, action='list')
                    d_call = parseAllele(call_str, d_allele_regex, action='list')
                    j_call = parseAllele(call_str, j_allele_regex, action='list')
                    db_gen['V_CALL'] = ','.join(v_call) if v_call is not None else 'None'
                    db_gen['D_CALL'] = ','.join(d_call) if d_call is not None else 'None'
                    db_gen['J_CALL'] = ','.join(j_call) if j_call is not None else 'None'

                    # Parse junction sequence
                    # db_gen['JUNCTION_VDJ'] = re.sub('(N/A)|\[|\(|\)|\]', '', ''.join(block_list[1]))
                    # db_gen['JUNCTION_LENGTH_VDJ'] = len(db_gen['JUNCTION_VDJ'])

                    # TODO:  IgBLAST does a stupid and doesn't output block #3 sometimes. why?
                    # TODO:  maybe we should fail these. they look craptastic.
                    #pd.set_option('display.width', 500)
                    #print query_name, len(block_list), hit_idx
                    #for i, x in enumerate(block_list):
                    #    print '[%i]' % i
                    #    print x

                    # Parse segment start and stop positions
                    hit_df = block_list[-1]

                    # Alignment info block
                    #  0:  segment
                    #  1:  query id
                    #  2:  subject id
                    #  3:  % identity
                    #  4:  alignment length
                    #  5:  mismatches
                    #  6:  gap opens
                    #  7:  gaps
                    #  8:  q. start
                    #  9:  q. end
                    # 10:  s. start
                    # 11:  s. end
                    # 12:  evalue
                    # 13:  bit score
                    # 14:  query seq
                    # 15:  subject seq
                    # 16:  btop

                    # If V call exists, parse V alignment information
                    seq_vdj = ''
                    if v_call is not None:
                        v_align = hit_df[hit_df[0] == 'V'].iloc[0]
                        # Germline positions
                        db_gen['V_GERM_START_VDJ'] = int(v_align[10])
                        db_gen['V_GERM_LENGTH_VDJ'] = int(v_align[11]) - db_gen['V_GERM_START_VDJ'] + 1
                        # Query sequence positions
                        db_gen['V_SEQ_START'] = int(v_align[8])
                        db_gen['V_SEQ_LENGTH'] = int(v_align[9]) - db_gen['V_SEQ_START'] + 1

                        if int(v_align[6]) == 0:
                            db_gen['INDELS'] = 'F'
                        else:
                            db_gen['INDELS'] = 'T'
                            # Set functional to none so record gets tossed (junction will be wrong)
                            # db_gen['FUNCTIONAL'] = None

                        # V alignment scores
                        if score_fields:
                            try: db_gen['V_SCORE'] = float(v_align[13])
                            except (TypeError, ValueError): db_gen['V_SCORE'] = 'None'

                            try: db_gen['V_IDENTITY'] = float(v_align[3]) / 100.0
                            except (TypeError, ValueError): db_gen['V_IDENTITY'] = 'None'

                            try: db_gen['V_EVALUE'] = float(v_align[12])
                            except (TypeError, ValueError): db_gen['V_EVALUE'] = 'None'

                            try: db_gen['V_BTOP'] = v_align[16]
                            except (TypeError, ValueError): db_gen['V_BTOP'] = 'None'

                        # Update VDJ sequence, removing insertions
                        start = 0
                        for m in re.finditer(r'-', v_align[15]):
                            ins = m.start()
                            seq_vdj += v_align[14][start:ins]
                            start = ins + 1
                        seq_vdj += v_align[14][start:]

                    # TODO:  needs to check that the V results are present before trying to determine NP1_LENGTH from them.
                    # If D call exists, parse D alignment information
                    if d_call is not None:
                        d_align = hit_df[hit_df[0] == 'D'].iloc[0]

                        # TODO:  this is kinda gross.  not sure how else to fix the alignment overlap problem though.
                        # Determine N-region length and amount of J overlap with V or D alignment
                        overlap = 0
                        if v_call is not None:
                            np1_len = int(d_align[8]) - (db_gen['V_SEQ_START'] + db_gen['V_SEQ_LENGTH'])
                            if np1_len < 0:
                                db_gen['NP1_LENGTH'] = 0
                                overlap = abs(np1_len)
                            else:
                                db_gen['NP1_LENGTH'] = np1_len
                                n1_start = (db_gen['V_SEQ_START'] + db_gen['V_SEQ_LENGTH']-1)
                                n1_end = int(d_align[8])-1
                                seq_vdj += db_gen['SEQUENCE_INPUT'][n1_start:n1_end]

                        # Query sequence positions
                        db_gen['D_SEQ_START'] = int(d_align[8]) + overlap
                        db_gen['D_SEQ_LENGTH'] = max(int(d_align[9]) - db_gen['D_SEQ_START'] + 1, 0)

                        # Germline positions
                        db_gen['D_GERM_START'] = int(d_align[10]) + overlap
                        db_gen['D_GERM_LENGTH'] = max(int(d_align[11]) - db_gen['D_GERM_START'] + 1, 0)

                        # Update VDJ sequence, removing insertions
                        start = overlap
                        for m in re.finditer(r'-', d_align[15]):
                            ins = m.start()
                            seq_vdj += d_align[14][start:ins]
                            start = ins + 1
                        seq_vdj += d_align[14][start:]

                    # TODO:  needs to check that the V results are present before trying to determine NP1_LENGTH from them.
                    # If J call exists, parse J alignment information
                    if j_call is not None:
                        j_align = hit_df[hit_df[0] == 'J'].iloc[0]

                        # TODO:  this is kinda gross.  not sure how else to fix the alignment overlap problem though.
                        # Determine N-region length and amount of J overlap with V or D alignment
                        overlap = 0
                        if d_call is not None:
                            np2_len = int(j_align[8]) - (db_gen['D_SEQ_START'] + db_gen['D_SEQ_LENGTH'])
                            if np2_len < 0:
                                db_gen['NP2_LENGTH'] = 0
                                overlap = abs(np2_len)
                            else:
                                db_gen['NP2_LENGTH'] = np2_len
                                n2_start = (db_gen['D_SEQ_START']+db_gen['D_SEQ_LENGTH']-1)
                                n2_end = int(j_align[8])-1
                                seq_vdj += db_gen['SEQUENCE_INPUT'][n2_start:n2_end]
                        elif v_call is not None:
                            np1_len = int(j_align[8]) - (db_gen['V_SEQ_START'] + db_gen['V_SEQ_LENGTH'])
                            if np1_len < 0:
                                db_gen['NP1_LENGTH'] = 0
                                overlap = abs(np1_len)
                            else:
                                db_gen['NP1_LENGTH'] = np1_len
                                n1_start = (db_gen['V_SEQ_START']+db_gen['V_SEQ_LENGTH']-1)
                                n1_end = int(j_align[8])-1
                                seq_vdj += db_gen['SEQUENCE_INPUT'][n1_start:n1_end]
                        else:
                            db_gen['NP1_LENGTH'] = 0

                        # Query positions
                        db_gen['J_SEQ_START'] = int(j_align[8]) + overlap
                        db_gen['J_SEQ_LENGTH'] = max(int(j_align[9]) - db_gen['J_SEQ_START'] + 1, 0)

                        # Germline positions
                        db_gen['J_GERM_START'] = int(j_align[10]) + overlap
                        db_gen['J_GERM_LENGTH'] = max(int(j_align[11]) - db_gen['J_GERM_START'] + 1, 0)

                        # J alignment scores
                        if score_fields:
                            try: db_gen['J_SCORE'] = float(j_align[13])
                            except (TypeError, ValueError): db_gen['J_SCORE'] = 'None'

                            try: db_gen['J_IDENTITY'] = float(j_align[3]) / 100.0
                            except (TypeError, ValueError): db_gen['J_IDENTITY'] = 'None'

                            try: db_gen['J_EVALUE'] = float(j_align[12])
                            except (TypeError, ValueError): db_gen['J_EVALUE'] = 'None'

                            try: db_gen['J_BTOP'] = j_align[16]
                            except (TypeError, ValueError): db_gen['J_BTOP'] = 'None'

                        # Update VDJ sequence, removing insertions
                        start = overlap
                        for m in re.finditer(r'-', j_align[15]):
                            ins = m.start()
                            seq_vdj += j_align[14][start:ins]
                            start = ins + 1
                        seq_vdj += j_align[14][start:]

                    db_gen['SEQUENCE_VDJ'] = seq_vdj

                    # Create IMGT-gapped sequence and infer IMGT junction
                    if v_call is not None:
                        db_gen = gapV(db_gen, repo_dict)
                        if j_call is not None:
                            db_gen = getIMGTJunc(db_gen, repo_dict)

                    # FWR and CDR regions
                    if region_fields: getRegions(db_gen)

                yield IgRecord(db_gen)


# TODO:  should be more readable
def readIMGT(imgt_files, score_fields=False, region_fields=False, junction_fields=False):
    """
    Reads IMGT/HighV-Quest output

    Arguments: 
    imgt_files = IMGT/HighV-Quest output files 1, 2, 3, and 6
    score_fields = if True parse alignment scores
    region_fields = if True add FWR and CDR region fields
    junction_fields = if True add N1_LENGTH, N2_LENGTH, P3V_LENGTH, P5D_LENGTH,
                        P3D_LENGTH, P5J_LENGTH and D_FRAME junction fields
    
    Returns: 
    a generator of dictionaries containing alignment data
    """
    # Functionality parser
    def _functional(x):
        if x.startswith('productive'):  return 'T'
        elif x.startswith('unproductive'):  return 'F'
        else:  return None

    # junction frame parser
    def _inframe(x):
        if x == 'in-frame':  return 'T'
        elif x == 'out-of-frame':  return 'F'
        else:  return None

    imgt_iters = [csv.DictReader(open(f, 'rU'), delimiter='\t') for f in imgt_files]
    # Create a dictionary for each sequence alignment and yield its generator
    for sm, gp, nt, jn in zip(*imgt_iters):
        if len(set([sm['Sequence ID'],
                    gp['Sequence ID'],
                    nt['Sequence ID'],
                    jn['Sequence ID']])) != 1:
            sys.exit('Error: IMGT files are corrupt starting with Summary file record %s' \
                     % sm['Sequence ID'])

        db_gen = {'SEQUENCE_ID': sm['Sequence ID'],
                  'SEQUENCE_INPUT': sm['Sequence']}

        if 'No results' not in sm['Functionality']:
            # Functionality
            db_gen['FUNCTIONAL'] = _functional(sm['Functionality'])
            db_gen['IN_FRAME'] = _inframe(sm['JUNCTION frame'])
            db_gen['STOP'] = 'T' if 'stop codon' in sm['Functionality comment'] else 'F'
            db_gen['MUTATED_INVARIANT'] = 'T' if any(('missing' in sm['Functionality comment'],
                                                      'missing' in sm['V-REGION potential ins/del'])) else 'F'
            db_gen['INDELS'] = 'T' if any((sm['V-REGION potential ins/del'],
                                           sm['V-REGION insertions'],
                                           sm['V-REGION deletions'])) else 'F'

            # Sequences
            db_gen['SEQUENCE_VDJ'] = nt['V-D-J-REGION'] if nt['V-D-J-REGION'] else nt['V-J-REGION']
            db_gen['SEQUENCE_IMGT'] = gp['V-D-J-REGION'] if gp['V-D-J-REGION'] else gp['V-J-REGION']
            db_gen['JUNCTION_LENGTH'] = len(jn['JUNCTION']) if jn['JUNCTION'] else 0
            db_gen['JUNCTION'] = jn['JUNCTION']

            # Gene calls
            db_gen['V_CALL'] = re.sub('\sor\s', ',', re.sub(',', '', gp['V-GENE and allele']))
            db_gen['D_CALL'] = re.sub('\sor\s', ',', re.sub(',', '', gp['D-GENE and allele']))
            db_gen['J_CALL'] = re.sub('\sor\s', ',', re.sub(',', '', gp['J-GENE and allele']))

            # V-segment alignment positions
            v_seq_length = len(nt['V-REGION']) if nt['V-REGION'] else 0
            db_gen['V_SEQ_START'] = nt['V-REGION start']
            db_gen['V_SEQ_LENGTH'] = v_seq_length
            db_gen['V_GERM_START_IMGT'] = 1
            db_gen['V_GERM_LENGTH_IMGT'] = len(gp['V-REGION']) if gp['V-REGION'] else 0

            # Junction alignment positions
            db_gen['NP1_LENGTH'] = sum(int(i) for i in [jn["P3'V-nt nb"],
                                                       jn['N-REGION-nt nb'],
                                                       jn['N1-REGION-nt nb'],
                                                       jn["P5'D-nt nb"]] if i)
            db_gen['D_SEQ_START'] = sum(int(i) for i in [nt['V-REGION start'],
                                                         v_seq_length,
                                                         jn["P3'V-nt nb"],
                                                         jn['N-REGION-nt nb'],
                                                         jn['N1-REGION-nt nb'],
                                                         jn["P5'D-nt nb"]] if i)
            db_gen['D_SEQ_LENGTH'] = int(jn["D-REGION-nt nb"] or 0)
            db_gen['D_GERM_START'] = int(jn["5'D-REGION trimmed-nt nb"] or 0) + 1
            db_gen['D_GERM_LENGTH'] = int(jn["D-REGION-nt nb"] or 0)
            db_gen['NP2_LENGTH'] = sum(int(i) for i in [jn["P3'D-nt nb"],
                                                       jn['N2-REGION-nt nb'],
                                                       jn["P5'J-nt nb"]] if i)

            # J-segment alignment positions
            db_gen['J_SEQ_START'] = sum(int(i) for i in [nt['V-REGION start'], 
                                                         v_seq_length,
                                                         jn["P3'V-nt nb"],
                                                         jn['N-REGION-nt nb'],
                                                         jn['N1-REGION-nt nb'],
                                                         jn["P5'D-nt nb"],
                                                         jn["D-REGION-nt nb"],
                                                         jn["P3'D-nt nb"],
                                                         jn['N2-REGION-nt nb'],
                                                         jn["P5'J-nt nb"]] if i)
            db_gen['J_SEQ_LENGTH'] = len(nt['J-REGION']) if nt['J-REGION'] else 0
            db_gen['J_GERM_START'] = int(jn["5'J-REGION trimmed-nt nb"] or 0) + 1
            db_gen['J_GERM_LENGTH'] = len(gp['J-REGION']) if gp['J-REGION'] else 0

            # Alignment scores
            if score_fields:
                try:  db_gen['V_SCORE'] = float(sm['V-REGION score'])
                except (TypeError, ValueError):  db_gen['V_SCORE'] = 'None'

                try:  db_gen['V_IDENTITY'] = float(sm['V-REGION identity %']) / 100.0
                except (TypeError, ValueError):  db_gen['V_IDENTITY'] = 'None'

                try:  db_gen['J_SCORE'] = float(sm['J-REGION score'])
                except (TypeError, ValueError):  db_gen['J_SCORE'] = 'None'

                try:  db_gen['J_IDENTITY'] = float(sm['J-REGION identity %']) / 100.0
                except (TypeError, ValueError):  db_gen['J_IDENTITY'] = 'None'

            # FWR and CDR regions
            if region_fields: getRegions(db_gen)
            
            # D Frame and junction fields
            if junction_fields:
                db_gen['D_FRAME'] = int(jn['D-REGION reading frame'] or 0)
                db_gen['N1_LENGTH'] = sum(int(i) for i in [jn['N-REGION-nt nb'],
                                                           jn['N1-REGION-nt nb']] if i)
                db_gen['N2_LENGTH'] = int(jn['N2-REGION-nt nb'] or 0)
                db_gen['P3V_LENGTH'] = int(jn['P3\'V-nt nb'] or 0)
                db_gen['P5D_LENGTH'] = int(jn['P5\'D-nt nb'] or 0)    
                db_gen['P3D_LENGTH'] = int(jn['P3\'D-nt nb'] or 0)  
                db_gen['P5J_LENGTH'] = int(jn['P5\'J-nt nb'] or 0)  

        else:
            db_gen['V_CALL'] = 'None'
            db_gen['D_CALL'] = 'None'
            db_gen['J_CALL'] = 'None'

        yield IgRecord(db_gen)

    
# TODO:  should be more readable
def readIHMM(ihmm_output, seq_dict, repo_dict,
             score_fields=False, region_fields=False):
    """
    Reads iHMMuneAlign output

    Arguments:
    ihmm_output = iHMMuneAlign output file
    seq_dict = a dictionary of {ID:Seq} from input fasta file
    repo_dict = dictionary of IMGT gapped germline sequences
    score_fields = if True parse alignment scores
    region_fields = if True add FWR and CDR region fields

    Returns:
    a generator of dictionaries containing alignment data
    """
    # iHMMuneAlign columns
    # Courtesy of Katherine Jackson
    #
    #  1: Identifier - sequence identifer from FASTA input file
    #  2: IGHV - IGHV gene match from the IGHV repertoire, if multiple genes had equally
    #            good alignments both will be listed, if indels were found this will be
    #            listed, in case of multiple IGHV all further data is reported with
    #            respect to the first listed gene
    #  3: IGHD - IGHD gene match, if no IGHD could be found or the IGHD that was found
    #            failed to meet confidence criteria this will be 'NO_DGENE_ALIGNMENT'
    #  4: IGHJ - IGHJ gene match, only a single best matching IGHJ is reported, if indels
    #            are found then 'indel' will be listed
    #  5: V-REGION - portion of input sequence that matches to the germline IGHV, were
    #                nucleotide are missing at start or end the sequence is padded back
    #                to full length with '.' (the exonuclease loss from the end of the
    #                gene will therefore be equal to the number of '.' characters at the
    #                5` end), mismatches between germline and rearranged are in uppercase,
    #                matches are in lowercase
    #  6: N1-REGION - sequence between V- and D-REGIONs
    #  7: D-REGION - portion of input sequence that matches to the germline IGHD
    #                (model doesn't currently permit indels in the IGHD), where IGHD is
    #                reported as 'NO_DGENE_ALIGNMENT' this field contains all nucleotides
    #                between the V- and J-REGIONs
    #  8: N2-REGION - sequence between D- and J-REGIONs
    #  9: J-REGION - portion of the input sequence that matches germline IGHJ, padded
    #                5` and 3` to length of germline match
    # 10: V mutation count - count of mismatches in the V-REGION
    # 11: D mutation count - count of mismatches in the D-REGION
    # 12: J mutation count - count of mismatches in the J-REGION
    # 13: count of ambigious nts - count of 'n' or 'x' nucleotides in the input sequence
    # 14: IGHJ in-frame - 'true' is IGHJ is in-frame and 'false' if IGHJ is out-of-frame,
    #                     WARNING indels and germline IGHV database sequences that are
    #                     not RF1 can cause this to report inaccurately
    # 15: IGHV start offset - offset for start of alignment between input sequence and
    #                         germline IGHV
    #                         NOTE: appears to be base 1 indexing.
    # 16: stop codons - count of stop codons in the sequence, WARNING indels and germline
    #                   IGHV database sequence that are not RF can cause this to be inaccurate
    # 17: IGHD probability - probability that N-nucleotide addition could have created the
    #                        D-REGION sequence
    # 18: HMM path score - path score from HMM
    # 19: reverse complement - 0 for no reverse complement, 1 if alignment was to reverse
    #                          complement NOTE currently this version only functions with
    #                          input in coding orientation
    # 20: mutations in common region - count of mutations in common region, which is a
    #                                  portion of the IGHV that is highly conserved,
    #                                  mutations in this region are used to set various
    #                                  probabilities in the HMM
    # 21: ambigious nts in common region - count of 'n' or 'x' nucleotides in the
    #                                      common region
    # 22: IGHV start offset  - offset for start of alignment between input sequence and
    #                          germline IGHV
    #                          NOTE: appears to be base 0 indexing.
    #                          NOTE: don't know if this differs from 15; it doesn't appear to.
    # 23: IGHV gene length - length of IGHV gene
    # 24: A score - A score probability is calculated from the common region mutations
    #               and is used for HMM calculations relating to expected mutation
    #               probability at different positions in the rearrangement
    record_headers = ['SEQUENCE_ID',
                      'V_CALL',
                      'D_CALL',
                      'J_CALL',
                      'V_SEQ',
                      'NP1_SEQ',
                      'D_SEQ',
                      'NP2_SEQ',
                      'J_SEQ',
                      'V_MUT',
                      'D_MUT',
                      'J_MUT',
                      'NX_COUNT',
                      'J_INFRAME',
                      'V_SEQ_START',
                      'STOP_COUNT',
                      'D_PROB',
                      'HMM_SCORE',
                      'RC',
                      'COMMON_MUT',
                      'COMMON_NX_COUNT',
                      'V_SEQ_START2',
                      'V_SEQ_LENGTH',
                      'A_SCORE']

    record_handle = open(ihmm_output, 'rU')
    csv.register_dialect('semicol', delimiter=';', quotechar='"')
    records = csv.DictReader(record_handle, fieldnames=record_headers, dialect='semicol')

    # loop through records
    for row in records:
        # Skip empty lines
        if not row:
            continue

        # Process row if not empty
        db = {'SEQUENCE_ID': row['SEQUENCE_ID'],
              'SEQUENCE_INPUT': seq_dict[row['SEQUENCE_ID']]}

        if not row['V_CALL'] or row['V_CALL'].startswith('NA - ') or \
                row['V_CALL'].startswith('State path'):
            db['FUNCTIONAL'] = None
            db['V_CALL'] = None
            yield IgRecord(db)
            continue

        # Check stop codons
        db['FUNCTIONAL'] = 'F' if int(row['STOP_COUNT']) > 0 else 'T'

        # Check whether J is in-frame
        if row['J_INFRAME'] != 'true':
            db['IN_FRAME'] = 'F'
            db['FUNCTIONAL'] = 'F'

        # Check for indels
        if re.search('\[indels\]', row['V_CALL'] + row['D_CALL'] + row['J_CALL']):
            db['INDELS'] = 'T'
        else:
            db['INDELS'] = 'F'

        # Find V-REGION
        v_call = parseAllele(row['V_CALL'], v_allele_regex, action='list')
        vkey = (v_call[0],)
        if vkey in repo_dict:
            db['V_CALL'] = ','.join(v_call) if v_call is not None else 'None'
            sample_vseq = (row['V_SEQ']).strip('.')
            db['V_SEQ_START'] = int(row['V_SEQ_START'])
            db['V_SEQ_LENGTH'] = len(sample_vseq)
        else:
            yield IgRecord(db)
            continue

        # Find D-REGION
        if not row['D_CALL'] or row['D_CALL'] == 'NO_DGENE_ALIGNMENT':
            dgene, sample_dseq = 'NA', ''
        else:
            d_call = parseAllele(row['D_CALL'], d_allele_regex, action='list')
            dkey = (d_call[0],)
            if dkey in repo_dict:
                db['D_CALL'] = ','.join(d_call) if d_call is not None else 'None'
                sample_dseq = (row['D_SEQ']).strip('.')
                db['D_GERM_START'] = len(row['D_SEQ']) - len((row['D_SEQ']).lstrip('.'))
                db['D_GERM_LENGTH'] = len(sample_dseq)
            else:
                yield IgRecord(db)
                continue

        # Find J-REGION
        if not row['J_CALL'] or row['J_CALL'] == 'NO_JGENE_ALIGNMENT':
            db['FUNCTIONAL'] = 'F'
            db['J_CALL'] = ''
            yield IgRecord(db)
            continue
        else:
            j_call = parseAllele(row['J_CALL'], j_allele_regex, action='list')
            jkey = (j_call[0],)
            if jkey in repo_dict:
                db['J_CALL'] = ','.join(j_call) if j_call is not None else 'None'
                sample_jseq = (row['J_SEQ']).strip('.')
                db['J_GERM_START'] = len(row['J_SEQ']) - len((row['J_SEQ']).lstrip('.'))
                db['J_GERM_LENGTH'] = len(sample_jseq)
            else:
                yield IgRecord(db)
                continue

        # Assemble sample sequence
        db['SEQUENCE_VDJ'] = ''.join([sample_vseq,
                                      row['NP1_SEQ'],
                                      sample_dseq,
                                      row['NP2_SEQ'],
                                      sample_jseq])

        # Germline positions
        db['V_GERM_START_VDJ'] = 1
        db['V_GERM_LENGTH_VDJ'] = len(sample_vseq)

        # N/P lengths
        db['NP1_LENGTH'] = len(row['NP1_SEQ'])
        db['NP2_LENGTH'] = len(row['NP2_SEQ'])

        # D positions
        db['D_SEQ_START'] = sum(int(i) for i in [db['V_SEQ_START'],
                                                 db['V_SEQ_LENGTH'],
                                                 db['NP1_LENGTH']] if i)
        db['D_SEQ_LENGTH'] = len(sample_dseq)

        # J positions
        db['J_SEQ_START'] = sum(int(i) for i in [db['V_SEQ_START'],
                                                 db['V_SEQ_LENGTH'],
                                                 db['NP1_LENGTH'],
                                                 db['D_SEQ_LENGTH'],
                                                 db['NP2_LENGTH']] if i)
        db['J_SEQ_LENGTH'] = len(sample_jseq)

        # Add IMGT gapped sequence
        db = gapV(db, repo_dict)
        # Extract junction regions
        db = getIMGTJunc(db, repo_dict)

         # Overall alignment score
        if score_fields:
            try: db['HMM_SCORE'] = float(row['HMM_SCORE'])
            except (TypeError, ValueError): db['HMM_SCORE'] = ''

        # FWR and CDR regions
        if region_fields: getRegions(db)

        yield IgRecord(db)


def getIDforIMGT(seq_file):
    """
    Create a sequence ID translation using IMGT truncation
    
    Arguments: 
    seq_file = a fasta file of sequences input to IMGT
                    
    Returns: 
    a dictionary of {truncated ID: full seq description} 
    """
    
    # Create a seq_dict ID translation using IDs truncate up to space or 50 chars
    ids = {}
    for i, rec in enumerate(SeqIO.parse(seq_file, 'fasta', IUPAC.ambiguous_dna)):
        if len(rec.description) <= 50:
            id_key = rec.description
        else:
            id_key = re.sub('\||\s|!|&|\*|<|>|\?','_',rec.description[:50])
        ids.update({id_key:rec.description})

    return ids


def writeDb(db_gen, file_prefix, total_count, id_dict={}, no_parse=True,
            score_fields=False, region_fields=False, junction_fields=False,
            out_args=default_out_args):
    """
    Writes tab-delimited database file in output directory
    
    Arguments:
    db_gen = a generator of IgRecord objects containing alignment data
    file_prefix = directory and prefix for CLIP tab-delim file
    total_count = number of records (for progress bar)
    id_dict = a dictionary of {IMGT ID: full seq description}
    no_parse = if ID is to be parsed for pRESTO output with default delimiters
    score_fields = if True add alignment score fields to output file
    region_fields = if True add FWR and CDR region fields to output file
    junction_fields = if True add D FRAME junction field to output file
    out_args = common output argument dictionary from parseCommonArgs

    Returns:
    None
    """
    pass_file = "%s_db-pass.tab" % file_prefix
    fail_file = "%s_db-fail.tab" % file_prefix
    ordered_fields = ['SEQUENCE_ID',
                      'SEQUENCE_INPUT',
                      'FUNCTIONAL',
                      'IN_FRAME',
                      'STOP',
                      'MUTATED_INVARIANT',
                      'INDELS',
                      'V_CALL',
                      'D_CALL',
                      'J_CALL',
                      'SEQUENCE_VDJ',
                      'SEQUENCE_IMGT',
                      'V_SEQ_START',
                      'V_SEQ_LENGTH',
                      'V_GERM_START_VDJ',
                      'V_GERM_LENGTH_VDJ',
                      'V_GERM_START_IMGT',
                      'V_GERM_LENGTH_IMGT',
                      'NP1_LENGTH',
                      'D_SEQ_START',
                      'D_SEQ_LENGTH',
                      'D_GERM_START',
                      'D_GERM_LENGTH',
                      'NP2_LENGTH',
                      'J_SEQ_START',
                      'J_SEQ_LENGTH',
                      'J_GERM_START',
                      'J_GERM_LENGTH',
                      'JUNCTION_LENGTH',
                      'JUNCTION']

    if score_fields:
        ordered_fields.extend(['V_SCORE',
                               'V_IDENTITY',
                               'V_EVALUE',
                               'V_BTOP',
                               'J_SCORE',
                               'J_IDENTITY',
                               'J_EVALUE',
                               'J_BTOP',
                               'HMM_SCORE'])

    if region_fields:
        ordered_fields.extend(['FWR1_IMGT', 'FWR2_IMGT', 'FWR3_IMGT', 'FWR4_IMGT',
                               'CDR1_IMGT', 'CDR2_IMGT', 'CDR3_IMGT'])

    if junction_fields:
        ordered_fields.extend(['N1_LENGTH', 'N2_LENGTH', 
                               'P3V_LENGTH', 'P5D_LENGTH', 'P3D_LENGTH', 'P5J_LENGTH',
                               'D_FRAME'])

    # Not currently implemented
    # if ihmm_germ:
    #     ordered_fields.extend(['GERMLINE_IHMM', 'GERMLINE_IHMM_D_MASK'])

    # TODO:  This is not the best approach. should pass in output fields.
    # Initiate passed handle
    pass_handle = None

    # Open failed file
    if out_args['failed']:
        fail_handle = open(fail_file, 'wt')
        fail_writer = getDbWriter(fail_handle, add_fields=['SEQUENCE_ID', 'SEQUENCE_INPUT'])
    else:
        fail_handle = None
        fail_writer = None

    # Initialize counters and file
    pass_writer = None
    start_time = time()
    rec_count = pass_count = fail_count = 0
    for record in db_gen:
        #printProgress(i + (total_count/2 if id_dict else 0), total_count, 0.05, start_time)
        printProgress(rec_count, total_count, 0.05, start_time)
        rec_count += 1

        # Count pass or fail
        if (record.v_call == 'None' and record.j_call == 'None') or \
                record.functional is None or \
                not record.seq_vdj or \
                not record.junction:
            # print('\n', record.v_call, record.j_call, record.functional, record.junction)
            fail_count += 1
            if fail_writer is not None: fail_writer.writerow(record.toDict())
            continue
        else: 
            pass_count += 1
            
        # Build sample sequence description
        if record.id in id_dict:
            record.id = id_dict[record.id]

        # Parse sequence description into new columns
        if not no_parse:
            record.annotations = parseAnnotation(record.id, delimiter=out_args['delimiter'])
            record.id = record.annotations['ID']
            del record.annotations['ID']

        # TODO:  This is not the best approach. should pass in output fields.
        # If first sequence, use parsed description to create new columns and initialize writer
        if pass_writer is None:
            if not no_parse:  ordered_fields.extend(list(record.annotations.keys()))
            pass_handle = open(pass_file, 'wt')
            pass_writer = getDbWriter(pass_handle, add_fields=ordered_fields)

        # Write row to tab-delim CLIP file
        pass_writer.writerow(record.toDict())
    
    # Print log
    #printProgress(i+1 + (total_count/2 if id_dict else 0), total_count, 0.05, start_time)
    printProgress(rec_count, total_count, 0.05, start_time)

    log = OrderedDict()
    log['OUTPUT'] = pass_file
    log['PASS'] = pass_count
    log['FAIL'] = fail_count
    log['END'] = 'MakeDb'
    printLog(log)
    
    if pass_handle is not None: pass_handle.close()
    if fail_handle is not None: fail_handle.close()


# TODO:  may be able to merge with other mains
def parseIgBlast(igblast_output, seq_file, repo, no_parse=True, score_fields=False,
                 region_fields=False, out_args=default_out_args):
    """
    Main for IgBlast aligned sample sequences

    Arguments:
    igblast_output = IgBlast output file to process
    seq_file = fasta file input to IgBlast (from which to get sequence)
    repo = folder with germline repertoire files
    no_parse = if ID is to be parsed for pRESTO output with default delimiters
    score_fields = if True add alignment score fields to output file
    region_fields = if True add FWR and CDR region fields to output file
    out_args = common output argument dictionary from parseCommonArgs

    Returns:
    None
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDB'
    log['ALIGNER'] = 'IgBlast'
    log['ALIGN_RESULTS'] = os.path.basename(igblast_output)
    log['SEQ_FILE'] = os.path.basename(seq_file)
    log['NO_PARSE'] = no_parse
    log['SCORE_FIELDS'] = score_fields
    log['REGION_FIELDS'] = region_fields
    printLog(log)

    # Get input sequence dictionary
    seq_dict = getInputSeq(seq_file)

    # Formalize out_dir and file-prefix
    if not out_args['out_dir']:
        out_dir = os.path.split(igblast_output)[0]
    else:
        out_dir = os.path.abspath(out_args['out_dir'])
        if not os.path.exists(out_dir):  os.mkdir(out_dir)
    if out_args['out_name']:
        file_prefix = out_args['out_name']
    else:
        file_prefix = os.path.basename(os.path.splitext(igblast_output)[0])
    file_prefix = os.path.join(out_dir, file_prefix)

    total_count = countSeqFile(seq_file)

    # Create
    repo_dict = getRepo(repo)
    igblast_dict = readIgBlast(igblast_output, seq_dict, repo_dict,
                               score_fields=score_fields, region_fields=region_fields)
    writeDb(igblast_dict, file_prefix, total_count, no_parse=no_parse,
            score_fields=score_fields, region_fields=region_fields, out_args=out_args)


# TODO:  may be able to merge with other mains
def parseIMGT(imgt_output, seq_file=None, no_parse=True, score_fields=False,
              region_fields=False, junction_fields=False, out_args=default_out_args):
    """
    Main for IMGT aligned sample sequences

    Arguments:
    imgt_output = zipped file or unzipped folder output by IMGT
    seq_file = FASTA file input to IMGT (from which to get seqID)
    no_parse = if ID is to be parsed for pRESTO output with default delimiters
    score_fields = if True add alignment score fields to output file
    region_fields = if True add FWR and CDR region fields to output file
    out_args = common output argument dictionary from parseCommonArgs
        
    Returns: 
    None
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDb'
    log['ALIGNER'] = 'IMGT'
    log['ALIGN_RESULTS'] = imgt_output
    log['SEQ_FILE'] = os.path.basename(seq_file) if seq_file else ''
    log['NO_PARSE'] = no_parse
    log['SCORE_FIELDS'] = score_fields
    log['REGION_FIELDS'] = region_fields
    log['JUNCTION_FIELDS'] = junction_fields
    printLog(log)
    
    # Get individual IMGT result files
    temp_dir, imgt_files = extractIMGT(imgt_output)
        
    # Formalize out_dir and file-prefix
    if not out_args['out_dir']:
        out_dir = os.path.dirname(os.path.abspath(imgt_output))
    else:
        out_dir = os.path.abspath(out_args['out_dir'])
        if not os.path.exists(out_dir):  os.mkdir(out_dir)
    if out_args['out_name']:
        file_prefix = out_args['out_name']
    else:
        file_prefix = os.path.splitext(os.path.split(os.path.abspath(imgt_output))[1])[0]
    file_prefix = os.path.join(out_dir, file_prefix)

    total_count = countDbFile(imgt_files[0])
    
    # Get (parsed) IDs from fasta file submitted to IMGT
    id_dict = getIDforIMGT(seq_file) if seq_file else {}
    
    # Create
    imgt_dict = readIMGT(imgt_files, score_fields=score_fields,
                         region_fields=region_fields, 
                         junction_fields=junction_fields)
    writeDb(imgt_dict, file_prefix, total_count, id_dict=id_dict, no_parse=no_parse,
            score_fields=score_fields, region_fields=region_fields, junction_fields=junction_fields, 
            out_args=out_args)

    # Delete temp directory
    rmtree(temp_dir)


# TODO:  may be able to merge with other mains
def parseIHMM(ihmm_output, seq_file, repo, no_parse=True, score_fields=False,
              region_fields=False, out_args=default_out_args):
    """
    Main for iHMMuneAlign aligned sample sequences

    Arguments:
    ihmm_output = iHMMuneAlign output file to process
    seq_file = fasta file input to iHMMuneAlign (from which to get sequence)
    repo = folder with germline repertoire files
    score_fields = if True parse alignment scores
    region_fields = if True add FWR and CDR region fields
    no_parse = if ID is to be parsed for pRESTO output with default delimiters
    out_args = common output argument dictionary from parseCommonArgs

    Returns:
    None
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDB'
    log['ALIGNER'] = 'iHMMuneAlign'
    log['ALIGN_RESULTS'] = os.path.basename(ihmm_output)
    log['SEQ_FILE'] = os.path.basename(seq_file)
    log['NO_PARSE'] = no_parse
    printLog(log)

    # Get input sequence dictionary
    seq_dict = getInputSeq(seq_file)

    # Formalize out_dir and file-prefix
    if not out_args['out_dir']:
        out_dir = os.path.split(ihmm_output)[0]
    else:
        out_dir = os.path.abspath(out_args['out_dir'])
        if not os.path.exists(out_dir):  os.mkdir(out_dir)
    if out_args['out_name']:
        file_prefix = out_args['out_name']
    else:
        file_prefix = os.path.basename(os.path.splitext(ihmm_output)[0])
    file_prefix = os.path.join(out_dir, file_prefix)

    total_count = countSeqFile(seq_file)

    # Create
    repo_dict = getRepo(repo)
    ihmm_dict = readIHMM(ihmm_output, seq_dict, repo_dict,
                         score_fields=score_fields, region_fields=region_fields)
    writeDb(ihmm_dict, file_prefix, total_count,
            score_fields=score_fields, region_fields=region_fields,
            no_parse=no_parse, out_args=out_args)


def getArgParser():
    """
    Defines the ArgumentParser

    Arguments: 
    None
                      
    Returns: 
    an ArgumentParser object
    """
    fields = dedent(
             '''
              output files:
                  db-pass
                      database of alignment records with functionality information,
                      V and J calls, and a junction region.
                  db-fail
                      database with records that fail due to no functionality information
                      (did not pass IMGT), no V call, no J call, or no junction region.

              universal output fields:
                  SEQUENCE_ID, SEQUENCE_INPUT, SEQUENCE_VDJ, SEQUENCE_IMGT,
                  FUNCTIONAL, IN_FRAME, STOP, MUTATED_INVARIANT, INDELS,
                  V_CALL, D_CALL, J_CALL,
                  V_SEQ_START, V_SEQ_LENGTH,
                  D_SEQ_START, D_SEQ_LENGTH, D_GERM_START, D_GERM_LENGTH,
                  J_SEQ_START, J_SEQ_LENGTH, J_GERM_START, J_GERM_LENGTH,
                  JUNCTION_LENGTH, JUNCTION, NP1_LENGTH, NP2_LENGTH,
                  FWR1_IMGT, FWR2_IMGT, FWR3_IMGT, FWR4_IMGT,
                  CDR1_IMGT, CDR2_IMGT, CDR3_IMGT

              imgt specific output fields:
                  V_GERM_START_IMGT, V_GERM_LENGTH_IMGT,
                  N1_LENGTH, N2_LENGTH, P3V_LENGTH, P5D_LENGTH, P3D_LENGTH, P5J_LENGTH,
                  D_FRAME, V_SCORE, V_IDENTITY, J_SCORE, J_IDENTITY,

              igblast specific output fields:
                  V_GERM_START_VDJ, V_GERM_LENGTH_VDJ,
                  V_EVALUE, V_SCORE, V_IDENTITY, V_BTOP,
                  J_EVALUE, J_SCORE, J_IDENTITY, J_BTOP

              ihmm specific output fields:
                  V_GERM_START_VDJ, V_GERM_LENGTH_VDJ,
                  HMM_SCORE
              ''')
                
    # Define ArgumentParser
    parser = ArgumentParser(description=__doc__, epilog=fields,
                            formatter_class=CommonHelpFormatter)
    parser.add_argument('--version', action='version',
                        version='%(prog)s:' + ' %s-%s' %(__version__, __date__))
    subparsers = parser.add_subparsers(title='subcommands', dest='command',
                                       help='Aligner used', metavar='')
    # TODO:  This is a temporary fix for Python issue 9253
    subparsers.required = True

    # Parent parser    
    parser_parent = getCommonArgParser(seq_in=False, seq_out=False, log=False)

    # IgBlast Aligner
    parser_igblast = subparsers.add_parser('igblast', parents=[parser_parent],
                                           formatter_class=CommonHelpFormatter,
                                           help='Process IgBLAST output.',
                                           description='Process IgBLAST output.')
    parser_igblast.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                                required=True,
                                help='''IgBLAST output files in format 7 with query sequence
                                     (IgBLAST argument \'-outfmt "7 std qseq sseq btop"\').''')
    parser_igblast.add_argument('-r', nargs='+', action='store', dest='repo', required=True,
                                help='''List of folders and/or fasta files containing
                                     IMGT-gapped germline sequences corresponding to the
                                     set of germlines used in the IgBLAST alignment.''')
    parser_igblast.add_argument('-s', action='store', nargs='+', dest='seq_files',
                                required=True,
                                help='List of input FASTA files containing sequences')
    parser_igblast.add_argument('--noparse', action='store_true', dest='no_parse',
                                help='''Specify if input IDs should not be parsed to add
                                     new columns to database.''')
    parser_igblast.add_argument('--scores', action='store_true', dest='score_fields',
                                help='''Specify if alignment score metrics should be
                                     included in the output. Adds the V_SCORE, V_IDENTITY,
                                     V_EVALUE, V_BTOP, J_SCORE, J_IDENTITY,
                                     J_BTOP, and J_EVALUE columns.''')
    parser_igblast.add_argument('--regions', action='store_true', dest='region_fields',
                                help='''Specify if IMGT framework and CDR regions should be
                                     included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                     FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                     CDR3_IMGT columns.''')
    parser_igblast.set_defaults(func=parseIgBlast)

    # IMGT aligner
    parser_imgt = subparsers.add_parser('imgt', parents=[parser_parent],
                                        formatter_class=CommonHelpFormatter,
                                        help='''Process IMGT/HighV-Quest output
                                             (does not work with V-QUEST).''',
                                        description='''Process IMGT/HighV-Quest output
                                             (does not work with V-QUEST).''')
    parser_imgt.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                             help='''Either zipped IMGT output files (.zip or .txz) or a
                                  folder containing unzipped IMGT output files (which must
                                  include 1_Summary, 2_IMGT-gapped, 3_Nt-sequences,
                                  and 6_Junction).''')
    parser_imgt.add_argument('-s', nargs='*', action='store', dest='seq_files',
                             required=False,
                             help='List of input FASTA files containing sequences')
    parser_imgt.add_argument('--noparse', action='store_true', dest='no_parse', 
                             help='''Specify if input IDs should not be parsed to add new
                                  columns to database.''')
    parser_imgt.add_argument('--scores', action='store_true', dest='score_fields',
                             help='''Specify if alignment score metrics should be
                                  included in the output. Adds the V_SCORE, V_IDENTITY,
                                  J_SCORE and J_IDENTITY. Note, this will also add
                                  the columns V_EVALUE, V_BTOP, J_EVALUE and J_BTOP,
                                  but they will be empty for IMGT output.''')
    parser_imgt.add_argument('--regions', action='store_true', dest='region_fields',
                             help='''Specify if IMGT framework and CDR regions should be
                                  included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                  FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                  CDR3_IMGT columns.''')
    parser_imgt.add_argument('--junction', action='store_true', dest='junction_fields',
                             help='''Specify if junction fields should be
                                  included in the output. Adds the columns 
                                  N1_LENGTH, N2_LENGTH, P3V_LENGTH, P5D_LENGTH, P3D_LENGTH,
                                  P5J_LENGTH, D_FRAME.''')
    parser_imgt.set_defaults(func=parseIMGT)

    # iHMMuneAlign Aligner
    parser_ihmm = subparsers.add_parser('ihmm', parents=[parser_parent],
                                        formatter_class=CommonHelpFormatter,
                                        help='Process iHMMuneAlign output.',
                                        description='Process iHMMuneAlign output.')
    parser_ihmm.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                             required=True,
                             help='''iHMMuneAlign output file.''')
    parser_ihmm.add_argument('-r', nargs='+', action='store', dest='repo', required=True,
                             help='''List of folders and/or fasta files containing
                                  IMGT-gapped germline sequences corresponding to the
                                  set of germlines used in the IgBLAST alignment.''')
    parser_ihmm.add_argument('-s', action='store', nargs='+', dest='seq_files',
                             required=True,
                             help='List of input FASTA files containing sequences')
    parser_ihmm.add_argument('--noparse', action='store_true', dest='no_parse',
                             help='''Specify if input IDs should not be parsed to add
                                  new columns to database.''')
    parser_ihmm.add_argument('--scores', action='store_true', dest='score_fields',
                             help='''Specify if alignment score metrics should be
                                  included in the output. Adds the path score of the
                                  iHMMuneAlign hidden Markov model to HMM_SCORE.''')
    parser_ihmm.add_argument('--regions', action='store_true', dest='region_fields',
                             help='''Specify if IMGT framework and CDR regions should be
                                  included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                  FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                  CDR3_IMGT columns.''')
    parser_ihmm.set_defaults(func=parseIHMM)

    return parser
    
    
if __name__ == "__main__":
    """
    Parses command line arguments and calls main
    """
    parser = getArgParser()    
    args = parser.parse_args()
    args_dict = parseCommonArgs(args, in_arg='aligner_files')

    # Set no ID parsing if sequence files are not provided
    if 'seq_files' in args_dict and not args_dict['seq_files']:
        args_dict['no_parse'] = True

    # Delete
    if 'seq_files' in args_dict: del args_dict['seq_files']
    if 'aligner_files' in args_dict: del args_dict['aligner_files']
    if 'command' in args_dict: del args_dict['command']
    if 'func' in args_dict: del args_dict['func']           
    
    if args.command == 'imgt':
        for i in range(len(args.__dict__['aligner_files'])):
            args_dict['imgt_output'] = args.__dict__['aligner_files'][i]
            args_dict['seq_file'] = args.__dict__['seq_files'][i] \
                                    if args.__dict__['seq_files'] else None
            args.func(**args_dict)
    elif args.command == 'igblast':
        for i in range(len(args.__dict__['aligner_files'])):
            args_dict['igblast_output'] =  args.__dict__['aligner_files'][i]
            args_dict['seq_file'] = args.__dict__['seq_files'][i]
            args.func(**args_dict)
    elif args.command == 'ihmm':
        for i in range(len(args.__dict__['aligner_files'])):
            args_dict['ihmm_output'] =  args.__dict__['aligner_files'][i]
            args_dict['seq_file'] = args.__dict__['seq_files'][i]
            args.func(**args_dict)
