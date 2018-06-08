#!/usr/bin/python3.5

# string exercise 2

str1 = ''

for letter in range(97, 108):
    str1 = str1 + chr(letter)

str2 = '21345'

try:
    str1[0] = 2
    print('cannot assign')
except:
    print('try error has occured')

str1 = '10' + str1[1:]

print(str1)
