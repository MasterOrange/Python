#!/usr/local/bin/python3.5

import re
import numpy

fncList = list(dir(re))

fncList.append('find')

fncList.sort()

#print(fncList)

# 'yield' is used for generators

# pass used as place holder

# from functools import partial
# allows you to feed the output of one function into another function
