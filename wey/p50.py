#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

= 997651
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

limit = 1000000
primes_list = prime_sieve(limit)
primes_set = set(primes_list)

max_count = 0
max_prime = 0

curSum = sum(primes_list)
N = L = len(primes_list)
p_pos = len(primes_list) / 2

# find the max starting length for N
# cut off the last prime if it exceeds limit
while curSum >= limit:
    N -= 1
    curSum -= primes_list[N]

while N > 0:
    N -= 1

    # sum of first N primes
    curSum = sum(primes_list[:N])
    head, tail = 0, N

    # do not recalculate consecutive sums, add next prime and substract first prime
    while curSum < limit and curSum not in primes_set and tail < L:
        curSum -= primes_list[head]
        curSum += primes_list[tail]
        head += 1
        tail += 1

    if curSum < limit and curSum in primes_set:
        print curSum
        break



# '''
print time.clock() - start_time


