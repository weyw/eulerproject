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

    # n = 6
    # n = 3
    n = 10001

    count = 1
    total = 0

    if n < 2:
        total = 2
    else:
        cur = 3
        while count < n:
            if is_prime(cur):
                count += 1
                total = cur
            cur += 2

    print(total)

print timeit.timeit(run, number=1)
