#!/usr/local/bin/python3.5

# searches for restriction sites in a sequence in fasta (includes complements)

import sys
import re

name, fasta, restr = sys.argv

compDict = {'A':'T','T':'A','C':'G','G':'C'}

seqList = []
siteList = []
seq = ''
comp = []


with open(sys.argv[1], 'r') as f:
    seqname = f.readline()
    next(f)
#    for line in f
#        line = line.rstrip('\n')
#        seqList.append(line)
    seqList = [line.rstrip('\n') for line in f]
seq = ''.join(seqList)
with open(sys.argv[2], 'r') as g:
#    for line in g:
#        line = line.rstrip('\n')
#        siteList.append(line)
    siteList = [line.rstrip('\n') for line in g]


def complements(seq):
# complement of the sequence
    for base in seq:
        comp.append(compDict[base])
    return ''.join(comp)

def restrFind():
# find regex of restriction sites
    locale = []
    revloc = []
    output = []
    for site in siteList:
        locale = [m.start() for m in re.finditer(site, seq)]
        revloc = [n.start() for n in re.finditer(site, complements(seq))]
        output = output + [site] + ['Forward: '] + locale + ['Reverse: '] + \
                 revloc + ['\n']
    output2 = [str(x) for x in output]
    print('\n'.join(output2))

restrFind()
