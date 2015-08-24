#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

= 5777
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

n = 8000
primes_set = prime_sieve(n)
for i in range(9, 10000, 2):
    flag = True
    for p in primes_set:
        if p > i:
            break
        x = math.sqrt((i - p) / 2)
        # print x - math.floor(x)
        if x - math.floor(x) == 0.0:
            flag = False
            break

    if flag:
        print i
        break



# '''
print time.clock() - start_time


