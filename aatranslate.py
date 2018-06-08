#!/usr/local/bin/python3.5

# Translates a fasts file in all 6 frames

import sys
# import pdb


# name, inFile = sys.argv

seqList = []
seqname = ''

with open(sys.argv[1], 'r') as f:
    seqname = f.readline()
    next(f)
    for line in f:
       line = line.rstrip('\n')
       seqList.append(line)
 
seq = ''.join(seqList)
seqname = seqname[:-3]

aaDict = {"AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N",
          "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
          "AGA":"R", "AGC":"S", "AGG":"R", "AGT":"S", 
          "ATA":"I", "ATC":"I", "ATG":"M", "ATT":"I",
          "CAA":"Q", "CAC":"H", "CAG":"Q", "CAT":"H",
          "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
          "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
          "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
          "GAA":"E", "GAC":"D", "GAG":"E", "GAT":"D",
          "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
          "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
          "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
          "TAA":"_", "TAC":"Y", "TAG":"_", "TAT":"T", "TCA":"S",
          "TCC":"S", "TCG":"S", "TCT":"S", "TGA":"_", "TGC":"C",
          "TGG":"W", "TGT":"C", "TTA":"L", "TTC":"F", "TTG":"L",
          "TTT":"F"}

def translates(mySeq):
    translated = []
    triplets = []
    transSeq = mySeq
    x = 0
    if len(transSeq)%3 == 1:
        transSeq = transSeq[:-1]
    elif len(transSeq)%3 == 2:
        transSeq = transSeq[:-2]
    else:
        pass
    while x < len(transSeq):
        triplets.append(transSeq[x:x+3])
        x += 3
    for item in triplets:      
        translated.append(aaDict[item])
#    print(''.join(translated))
    return ''.join(translated)

# pdb.set_trace()

# translates(seq)

def frameread():
    x = 0
    myseq = seq
    myList = []
    while x < 3:
        myList.append(translates(myseq))
        myseq = myseq[1:]
        x += 1
    revseq = seq[::-1]
    y = 0
    while y < 3:
        myList.append(translates(revseq))
        revseq = revseq[1:]
        y += 1
    print(seqname + '\n' + '\n'.join(myList))

frameread()


