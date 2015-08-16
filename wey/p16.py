'''
https://projecteuler.net/problem=16

= 1366
'''

import timeit
import math
import sys
from euler import *




def run():
    # n = 15
    n = 1000
    i = 2 ** n
    q = list(str(i))

    print (q, sum(map(int, q)))




print timeit.timeit(run, number=1)



