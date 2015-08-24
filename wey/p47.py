#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

=134043
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''


ci = 0
n = 1158

while ci != 4:
    n += 1
    ci = 0
    for j in range(4):
        if len(set(prime_factors(n + j))) == 4:
            ci += 1

print n




# '''
print time.clock() - start_time


