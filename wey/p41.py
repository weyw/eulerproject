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
from euler import *

start_time = time.clock()
''' '''

l = 98765431

primes_list = []
primes_set = set()
p_max = 0
file_name = "primes1.txt"
# file_name = ""

if file_name != "":
    with open(file_name) as f:
        for line in f:
            primes_list.extend(map(int, (i for i in line.split(" ") if i != '')))
else:
    primes_list = prime_sieve(1000000000)


# primes_set = set(primes_list)
for p in primes_list:
    if len(set(str(p))) == len(str(p)) and set('123456789'[:len(str(p))]) >= set(str(p)):
        if p > p_max:
            p_max = p

print p_max


# '''
print time.clock() - start_time


