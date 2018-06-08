#!/usr/bin/python3.5

# translates FASTQ into FASTA files

import sys
import gzip


name, inFile, outFile = sys.argv

def translator(inFile):
    if inFile.endswith('.gz'): #extract the file if in .gz form
        with gzip.open(inFile, 'rb') as f:
            unproc = []
            for line in f:
                unproc.append(line.decode("utf-8"))
            for line in unproc:
                if line == '+\n':
                    unproc.remove(line)
     #   for item in range(0,len(unproc)):
      #      if item%2 == 1:
       #         del unproc[item-1]
    #    proc = []
     #   proc.append(str(unproc[0]))
      #  proc[0] = '>' + proc[0][1:]
#    for item in proc:
#        if item == '\n':               
#            proc.remove(item)
     #   for v in range(1, len(unproc)):
     #       if v%4 == 0:
     #           proc.append(unproc[v-3])
     #   outFile = open(sys.argv[2]+'.fasta', 'w')
    #    for line in proc:
     #       outFile.write(line)
      #  outFile.close()
    else:
        with open(inFile) as f:
            unproc = f.read().splitlines()
    proc = []
    proc.append(str(unproc[0]))
    proc[0] = '>' + proc[0][1:]
#    for item in proc:
#        if item == '\n':               
#            proc.remove(item)
    for v in range(1, len(unproc)):
        if v%4 == 0:
            proc.append(unproc[v-3])
    outFile = open(sys.argv[2]+'.fasta', 'w')
    for line in proc:
        outFile.write('%s\n' % line)
    outFile.close()

translator(inFile)
