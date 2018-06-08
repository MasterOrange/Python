#!/usr/local/bin/python3.5

# program that generates random numbers

import random

Casey = 418
Steve = 682
Num = -1
Possible = 1000
NumList = []

while Num != Casey and Num !=Steve:
    Num = random.randint(0,Possible)
    NumList.append(Num)

print(NumList)
print(['Casey','Steve'][Num == Steve] + ' wins!!')

# Num == Steve prints Steve when Num is the same as Steve's number (True -> 1)
# prints Casey if False -> 0
