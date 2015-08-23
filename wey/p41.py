#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

= 7652413
in
'''

import time
import math
import sys
import itertools
from euler import *

start_time = time.clock()
''' '''


primes_list = []
primes_set = set()
file_name = "primes/primes1.txt"

with open(file_name) as f:
    for line in f:
        primes_list.extend(map(int, (i for i in line.split(" ") if i != '')))

primes_set = set(prime_sieve(8000000))
print max(int(i) for i in permute('1234567')
    if int(i) in primes_set)




# '''
print time.clock() - start_time


