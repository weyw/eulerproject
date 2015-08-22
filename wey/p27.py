#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=28

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

= -59231
'''

import time
import math
import sys
from euler import *

start_time = time.clock()

a_max = 0
b_max = 0
n_max = 0
L = [False] * 751000
P = prime_sieve(1000)
for p in P:
    L[p] = True

for a in range(-1001, 1000, 2):
    for b in range(1, 1000):
        # print a, b

        if b < -1600 - 40 * a or b < n_max or not L[b]:
            continue

        n = 0
        count = 0

        # print a, b, n
        if (n ** 2 + a * n + b) > 0 :
            while L[n ** 2 + a * n + b]:
                n += 1
                count += 1

            if count > n_max :
                a_max = a
                b_max = b
                n_max = count

print a_max, b_max, n_max, a_max * b_max

# '''
print time.clock() - start_time


