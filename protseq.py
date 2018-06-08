#!/usr/local/bin/python3.5

#takes protein and makes hydropathy, charge, and bulk
#runs R code to make a graph of the results
#runs protdb search on protein?

import argparse    #can also use sys but it has less functionality than argparse
import subprocess  #call R code from shell

#initiating argument parser
parser = argparse.ArgumentParser(description = 'Protein thingy')

#required argument
parser.add_argument('inFile', metavar = 'INFILE')                      #input file

#table of hydrophobicity movement
hydrolib = {'I':3.1, 'V':2.3, 'L':2.2, 'F':2.5,
            'C':0.2, 'M':1.1, 'A':1.0, 'G':0.7,
            'T':-0.8, 'S':-1.1, 'W':-1.5, 'Y':0.1,
            'P':-0.3, 'H':-1.7, 'E':-2.6, 'Q':-2.9,
            'D':-3.0, 'N':-2.7, 'K':-4.6, 'R':-7.5,
            '-':'NaN', '*':'NaN'}

#table of Ph equilibrium
chargelib = {'D':2.8, 'E':3.2, 'C':5.1, 'N':5.4, 'F':5.5,
             'Q':5.7, 'Y':5.7, 'S':5.7, 'M':5.7, 'T':5.9,
             'I':5.9, 'G':6.0, 'V':6.0, 'W':6.0, 'L':6.0,
             'A':6.0, 'P':6.5, 'H':7.6, 'K':9.7, 'R':10.8,
             '-':'NaN', '*':'NaN'}

#table of molecular weight
bulklib = {'A':89.10, 'R':174.20, 'N':132.12, 'D':133.11,
           'C':121.16, 'E':147.13, 'Q':146.15, 'G':75.07,
           'H':155.16, 'O':131.13, 'I':131.18, 'L':131.13,
           'K':146.19, 'M':146.21, 'F':165.19, 'P':115.13,
           'U':139.11, 'S':105.09, 'T':119.12, 'W':204.23,
           'Y':181.19, 'V':117.15}

args = parser.parse_args()

def hydropathy():
    sequence = []
    with open(args.inFile, 'r') as f:
        seqname = f.readline()
        next(f)
        for line in f:
            line = line.rstrip('\n')
            sequence.append(line)

    sequence = ''.join(sequence)
    #makes lists of all the properties
    position = ['position'] + [x+1 for x in range(len(sequence))]
    hydro_score = ['hydropathy'] + [hydrolib[x] for x in sequence]
    sequence2 = ['a.acid'] + list(sequence)
    bulk = ['MW'] + [bulklib[x] for x in sequence]
    charge = ['charge'] +[chargelib[x] for x in sequence]

    print(seqname)
#    #display the properties of the protein sequence
#    #print formatting, right aligned, 15 spaces
#    rform = '{:>11}'*5
#    combined = [sequence2, position, hydro_score, charge, bulk]
#    # unpacking
#    for item in zip(*combined):
#        print(rform.format(*item))

    with open('output.csv', 'w') as g:
        x = 0
        #making the csv file by collecting the nth item of list into each line
        while x < len(sequence2):
            g.write(sequence2[x] + ',' + str(position[x]) + ',' + str(hydro_score[x]) + ',' + 
                    str(charge[x]) + ',' + str(bulk[x]) + '\n')
            x += 1
#        for a, b, c, d, e in sequence2, position, hydro_score, charge, bulk:
#            g.write(a + ',' + b + ',' + c + ',' + d + ',' + e)

hydropathy()

if __name__ == '__main__':
    args = parser.parse_args()

subprocess.call("~/R/aaPlot/aaPlot.R", shell = True)

subprocess.call("xdg-open output_graph.png", shell = True)
