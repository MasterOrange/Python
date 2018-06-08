#!/usr/bin/python3.5

# counts Ts and everything else

sequence = input('input your sequence: \n')
proc = list(sequence)
Tcounter = 0
Ncounter = 0
for item in proc:
    print(str(item)+ ', ', end='')
    if item == 't':
       Tcounter = Tcounter + 1
    elif item != 't':
        Ncounter = Ncounter + 1
print('\nThere are ' + str(Tcounter) + ' T\'s and ' + str(Ncounter) + \
        ' other bases in the sequence.')


