'''
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

= 104743
'''

import timeit
import math
import sys
from euler import *

def run():

    # n = 1
    # n = 2
    n = 27
    # n = 10001



    print(prime_sieve(n))

print timeit.timeit(run, number=1)
