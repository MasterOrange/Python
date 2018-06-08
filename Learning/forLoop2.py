#!/usr/bin/python3.5

# stops at third T

sequence = input('input your sequence: \n')
counter = 0
proc = list(sequence)
for item in proc:
    print(str(item)+', ', end='')
    if item == 't':
        counter = counter + 1
        if counter == 3:
            print('\nThe third T is reached')
            break
print('Done')

