#!/usr/local/bin/python3.5

# creates an instance of the coalescent from 10 sequences

import random
import sys
import math

name, reps = sys.argv

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

#make_seq()

def make_seq2(n):
    seq = ['a' + str(y) for y in range(n)]
    return seq

def coalescent(num):
    #num is int that gives the number of sequences in population
    #sequence generator
    seqs = make_seq(num)
    k = len(seqs)
    times = []
    theta = 4 * random.randint(5,10)
    l = random.randint(20,50)
    muh_tree = {}

    print('k = ' + str(k) + '\n' +
          'l = ' + str(l) + '\n' +
          'theta = ' + str(theta))

    while k > 0:
        # generate exponential waiting time with the following rate
        pm_num = random.random()

        # the next exponential waiting time
        time = math.exp((k * (k - 1 + (l * theta)) / 2))
        times.append(time)

        # rate of coalescence
        p = (k - 1) / (k - 1 + l*theta)

        # rate of mutation
        m = theta/(theta + k - 1)

        print('generated pm_num: ' + str(pm_num))

        if m > pm_num > p: # mutation event
            k += 1
        elif pm_num < p:   # coalescent event
            
            k -= 1
        # coalescent event, pick two sequences to join
        a = [random.choice(seqs, 2)]
        # (randomly select one to be the next item)
        seqs.remove(a)
        a = random.choice(a)
        seqs.append(a)
        k -= 1

coalescent(sys.argv[1])
