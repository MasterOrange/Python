#!/usr/local/bin/python3.5

#makes primers of given animo acids

import random
import itertools as it
from collections import defaultdict

myDict = {"AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N",
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

aalist = [(value, key) for key, value in myDict.items()]

d = defaultdict(list)
for k, v in aalist:
    d[k].append(v)

d.pop('_', None)

def primers():
    head, tail = [], []
    x = 0
    while x < 5:
        #generate some amino acids
        head.append(random.choice(list(d)))
        tail.append(random.choice(list(d)))
        x += 1
    fwd, rev = [], []
    flist = [d[x] for x in head]
    rlist = [d[y] for y in tail]
    fwd = list(it.product(*flist))
    fwd2 = [''.join(map(str, i)) for i in fwd]
    rev = list(it.product(*rlist))
    rev2 = [''.join(map(str, e)) for e in rev]
#    for x in head:
#        fwd = [random.choice(d[x]) for x in head]
#    for y in tail:
#        rev = [random.choice(d[y]) for y in tail]
    print('Fwd: ' + '<' + ''.join(head) + '>\n' + '\t'.join(str(v) for v in fwd2) + '\n\n'
          'Rev: ' + '<' + ''.join(tail) + '>\n' + '\t'.join(str(w) for w in rev2))

primers()
