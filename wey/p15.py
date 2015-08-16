'''
https://projecteuler.net/problem=16

= 137846528820
'''

import timeit
import math
import sys
from euler import *




def run():
    r = 20

    print (math.factorial(2 * r) / (math.factorial(r) ** 2))




print timeit.timeit(run, number=1)



