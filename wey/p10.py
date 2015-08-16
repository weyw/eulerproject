'''
https://projecteuler.net/problem=10

= 142913828922
'''

import timeit
import math
import sys
from euler import *

def run():
    n = 2000000
    f = lambda x, y: x + y

    print(sum(prime_sieve2(n)))



print timeit.timeit(run, number=1)
