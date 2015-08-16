'''
https://projecteuler.net/problem=12
http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
= 76576500
'''

import timeit
import math
import sys
from euler import *

def run():
    found = False
    n = 10
    t_num = 0

    while not found :
        t_num = n * (n + 1) / 2
        if len(factors(t_num)) > 500 :
            found = True
            break
        n += 1

    print(n, t_num)



print timeit.timeit(run, number=1)
