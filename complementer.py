#!/usr/local/bin/python3.5

# gets complement of sequence

import sys
import string

compDict = {'A':'T','T':'A','C':'G','G':'C'}

def complements():
    seqList = []
    seq = ''
    comp = []
    with open(sys.argv[1], 'r') as f:
        seqname = f.readline()
        next(f)
        for line in f:
            line = line.rstrip('\n')
            seqList.append(line)
    seq = ''.join(seqList)
    seq = list(seq[::-1])
    for base in seq:
        comp.append(compDict[base])
    print(seqname + ''.join(comp))

complements()

#def complement2():
#    seqList = []
#    inSeq = 'ATCG'
#    outSeq = 'TAGC'
#    trans = string.maketrans(inSeq, outSeq)
#    with open(sys.argv[1], 'r') as f:
#        seqname = f.readline()
#        next(f)
#        for line in f:
#            line = line.rstrip('\n')
#            seqList.append(line)
#    seq = ''.join(seqList)
#    seq = list(seq[::-1])
#    print(seqname + seq.translate(trans))
# AttributeError: string has no atrribute maketrans
#complement2()
