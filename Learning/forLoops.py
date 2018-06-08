#!/usr/bin/python3.5

# reads string of DNA

sequence = input('input your sequence: \n')
proc = list(sequence)
for item in proc:
    print(str(item)+', ', end='')
    if item == 't':
        print('\nT is reached')
        break
print('finished')
