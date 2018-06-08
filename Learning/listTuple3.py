#!/usr/bin/python3.5

# list exercise 3

x = list(range(1, 21))
y = list(range(21, 26))
print(str(x))

x[20:20] = y[0:5] 
print(str(x))

x[0:5] = []
print((x))
