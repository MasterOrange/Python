#!/usr/local/bin/python3.5

import random

def random_gen():
    k = random.randint(5, 10)
    l = random.randint(15, 20)
    theta = random.randint(20, 30)
    while k > 1:
        p_num = random.random()
        p = (k-1)/(k-1+l*theta)
        if p_num < p:
            print('Done')
            k -= 1
        else:
            print(str(p_num) + ' is > than ' + str(p))

random_gen()
