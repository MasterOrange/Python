#!/usr/local/bin/python3.5

#tracks the number of repeats for x iterations

import random
import sys

#generate a repeat of nucelotides

nucl = ['A', 'T', 'C', 'G']

num = random.randint(3,10)

sequence = [random.choice(nucl) for i in range(num)]
sequence = ''.join(sequence)

def repeater(n=100, a=0.1):
    seqrep = sequence*10
    occur = []
    iteration = 0
    while iteration < int(n):
        c = random.randint(0,100) 
        if c < float(a)*100:
            b = bool(random.getrandbits(1))
            if b == True:
                seqrep += sequence
            else:
                seqrep = seqrep.replace(sequence, '', 1)
        else:
            pass
        occur.append(seqrep.count(sequence))
        iteration += 1
    print(seqrep)
    print(occur)

repeater(sys.argv[1], sys.argv[2])
