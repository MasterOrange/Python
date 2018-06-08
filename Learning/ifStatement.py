#!/usr/bin/python3.5

# reads nucleotides

letter = input('input your nucleotide: ')
if letter in ['a', 't', 'c', 'g', 'A', 'T', 'C', 'G']:
    print('You entered: ' + str(letter))
else:
    print('Other')
print('Done')


