#!/usr/local/bin/python3.5

# creaates an instance of the coalescent from 10 sequences

import random
import itertools as it

nucl = ['A', 'T', 'C', 'G']

#generate original sequence
ori_seq = [random.choice(nucl) for i in range(15)]

#generate 10 random sequence based on the original sequence

def make_seq():
    x, num = 0, 0
    seqs = []
    new_seq = ori_seq
    while x < 10:
        num = random.randint(0, len(ori_seq)-1)
        new_seq[num] = random.choice(nucl)
        seqs.append(''.join(new_seq))
        x +=1
    print(seqs)

make_seq()


