#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

= 121313
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''
def family(prime, rd, primes_set):
    c = 0
    for d in '0123456789':
        n = int(string.replace(prime, rd, d))
        if n > 100000 and n in primes_set:
            c += 1

    return c == 8

primes_set = set(prime_sieve(1000000))
found_primes = set()

for p in primes_set:
    if p > 100000 and str(p)[-1:] == '3':
        s = str(p)

        # for i in '012':
        #     if s.count(i) and family(s, i, primes_set):
        #         found_primes.add(s)
        if (s.count('0') == 3 and family(s, '0', primes_set)) or (s.count('1') == 3 and family(s, '1', primes_set)) or (s.count('2') == 3 and family(s, '2', primes_set)):
            print s

# print(min(found_primes))

# '''
print time.clock() - start_time


