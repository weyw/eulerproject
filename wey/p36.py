#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

= 55
'''

import time
import math
import sys
from euler import *

import itertools
start_time = time.clock()
''' '''

n = 1000100
prime_list = prime_sieve(n)
prime_set = set(prime_list)
count = set()
for p in prime_list:
    if p > 1000000:
        break
    circular = True

    c = str(p)
    for i in range(len(c) - 1):
        c = c[1:] + c[:1]
        if int(c) not in prime_set:
            circular = False
            break

    if circular :
        count.add(p)

print len(count)

# '''
print time.clock() - start_time


