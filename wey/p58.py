#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

= 26241
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''

sides = 3
num_primes = 0
# primes_set = set(prime_sieve(10000000))

x = 1502
# for sides in range(3, x, 2):
while True:
    n = sides ** 2

    for i in range(4):
        m = n - ((sides - 1) * i)

        # if m in primes_set:
        if MillerRabinPrimalityTest(m):
            num_primes += 1

    if num_primes / ((sides - 1) * 2.0 + 1) < 0.1:
        # print num_primes, ((sides - 1) * 2.0 + 1)
        # print sides, num_primes, num_primes / ((sides - 1) * 2.0 + 1)
        break

    sides += 2

print sides, num_primes, num_primes / ((sides - 1) * 2.0 + 1)
# print sides, num_primes, ((sides - 1) * 2.0 + 1), num_primes / ((sides - 1) * 2.0 + 1)




# '''
print time.clock() - start_time


