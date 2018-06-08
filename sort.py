#!/usr/bin/python3.5

# sorts numbers

import sys
# import pdb

# pdb.set_trace()

name, aFile, reverse = sys.argv

def my_sort(aFile):
    with open(aFile, 'r') as f:
        myFile = [line.strip() for line in f]
    toSort = []
    for line in myFile:
        toSort.append(int(line))
    for v in range(1, len(toSort)):
        val = v
        while val > 0 and toSort[val] < toSort[val-1]:
            toSort[val], toSort[val-1] = toSort[val-1], toSort[val]
            val = val - 1
    if sys.argv[2] == '-r':
        toSort.reverse()
        print(toSort)
    else:
        print(toSort)

my_sort(aFile)
