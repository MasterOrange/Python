#!/usr/bin/python3.5

# 
import argparse

parser = argparse.ArgumentParser()
parse.add_argument("-r", help = "Reverses the order of the sorting")
args = parser.parse_args()

def my_sort(aFile):
    with open(aFile, 'r') as f:
        myFile = [line.strip() for line in f]
    toSort = []

args.r:
    toSort.reverse()
    print(toSort)


