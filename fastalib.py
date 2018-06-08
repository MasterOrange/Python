#!/usr/local/bin/python3.5

# May 21, 2018 Makes a library of fasta files, makes blast database of library and runs blast on it
# June 04, 2018 makes tabular output from BLAST output format 6

import os
import argparse
import subprocess

#__location__ = os.path.realpath(
#        os.path.join(os.getcwd(), os.path.dirname(__file__)))

# initiating argument parser
parser = argparse.ArgumentParser(description = 'Some FASTA file functionalities')

# required argument
parser.add_argument('infile', metavar = 'InFile')          #input file  

# optional flags
parser.add_argument('-db', '--makedb', metavar = 'DBTYPE')
parser.add_argument('-b', '--blast', metavar = 'BLAST')    #runs blast
parser.add_argument('-a', '--append', metavar = 'APPEND')  #updates an outfile
parser.add_argument('-p', '--parser', metavar = 'TBPARSE') #parses data from BLAST -outfmt 6

# optional positional argument
parser.add_argument('outfile', metavar = 'OutFile', \
                     nargs = '?', default = 'output.txt')  #output file             

args = parser.parse_args()

def addFile(aFile):
# adds fasta to list of fast a files
    try:
        f = open(args.outfile, 'r')
    except:
        f = open(args.outfile, 'w')
    with open(args.outfile, 'a') as f:
        with open(aFile, 'r') as g:
                for line in g:
                    f.write(line)
    print(args.outfile + ' has been updated.')

def mkdb():
# makes blast database using subprocess.call(), input type is args.makedb
    subprocess.call(['makeblastdb', '-in', args.infile, '-parse_seqids', '-dbtype', args.makedb])
    print('Done')

def run_blast():
# runs blast on a user-specified file agianst another user-specified local blast database
    subprocess.call(['blastn', '-query', args.infile, '-db', args.outfile, '-outfmt', '6', '-out', 'blastn.out.txt'])
    print('Done')

def tab_parse():
    fileContent = [ ['qseqid'], ['sseqid'], ['pid'], ['len'], ['mismatch'], ['gopen'], ['qstart'], \
            ['qend'], ['sstart'], ['send'], ['evalue'], ['bitscore'] ]
    with open( args.infile, 'r' ) as f: #tab ( '\t' ) delimited
        for line in f:
            line.rstrip( '\n' )
            line = line.split( '\t' )
            for x in range( len( line ) ):
                fileContent[x].append( line[x] )
#    print( *['qseqid', 'sseqid', 'pid', 'len', 'mismatch', 'gopen', 'qstart', 'qend', \
#            'sstart', 'send', 'evalue', 'bitscore'], sep = '\t' )
#    print(fileContent)
    rform = '{:>15}'*len(fileContent)
    for item in zip( *fileContent ):
        print(rform.format( *item))



# what the optional arguments should do
if args.append:
    addFile(args.infile)
elif args.makedb:
    mkdb()
elif args.blast:
    run_blast()
elif args.parser:
    tab_parse()

# prints the names of all the sequences in the file
#with open(args.infile, 'r') as f:
#    for line in f:
#        if line[0] == '>':
#            print(line.rstrip('\n'))

if __name__ == '__main__':
    args = parser.parse_args()
