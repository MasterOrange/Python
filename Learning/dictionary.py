#!/usr/bin/python3.5

# dictionary exercise

keys = tuple(range(1, 20, 2))
defs = tuple(range(2, 21, 2))
myDict = {}

for item in keys:
    myDict[item] = defs[keys.index(item)]

print(str(myDict))

myDict[21] = 22

print(str(myDict))

del myDict[21]

print(str(myDict))

# dictionaries are unordered
