#!/usr/local/bin/python3.5

# searches for restriction sites within 1 bp

import sys
import re
from collections import OrderedDict

name, fasta, restr, opt  = sys.argv

compDict = {'A':'T','T':'A','C':'G','G':'C'}

seqList = []
siteList = []
seq = ''
# comp = []


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
    comp = []
    for base in seq:
        comp.append(compDict[base])
    comp = ''.join(comp[::-1])
    return comp

def wobbly():
# iteratively replace each character in given site with '\w'
    locale, localew, revloc, revlocw, output = [], [], [], [], []
    for site in siteList:
        locale = [str(m.start()) for m in re.finditer(site, seq)]
        revloc = [str(n.start()) for n in re.finditer(site, \
        complements(seq))]
        for base in site:
            site2 = site.replace(base, base+'\w')
            localew = [str(o.start())+'*' for o in re.finditer(site2, \
            seq)]
            revlocw = [str(p.start())+'*' for p in re.finditer(site2,\
            complements(seq))]
            locale += localew
            revloc += revlocw
        locale = list(OrderedDict.fromkeys(locale))
        revloc = list(OrderedDict.fromkeys(revloc))
        output = output + [site] + ['Forward: '] + locale + ['Reverse: '] + \
                 revloc + ['\n']
    print(seqname + '\n' + '\n'.join(output))

# wobbly()

def restrFind():
# find regex of restriction sites
    locale, revloc, output = [], [], []
    for site in siteList:
        locale = [m.start() for m in re.finditer(site, seq)]
        revloc = [n.start() for n in re.finditer(site, complements(seq))]
        output = output + [site] + ['Forward: '] + locale + ['Reverse: '] + \
                 revloc + ['\n']
    output2 = [str(x) for x in output]
    print('\n'.join(output2))

#restrFind()

if sys.argv[3] == '-w':
    wobbly()
else:
    restrFind()
