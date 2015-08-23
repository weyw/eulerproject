#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

= 748317
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

n = 1000000
primes_list = prime_sieve(n)
primes_set = set(primes_list)

total = set()

for p in primes_list:
    ps = str(p)
    if len(total) == 11:
        break
    if p > 11:
        all_prime = True
        for i in range(1, len(ps)):
            if int(ps[-1 * i:]) not in primes_set or int(ps[:i]) not in primes_set:
                all_prime = False
                break

        if all_prime:
            total.add(p)

print total, len(total), sum(total)

# '''
print time.clock() - start_time


