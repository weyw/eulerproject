#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

= 31626
'''

import timeit
import math
import sys
import datetime
from euler import *


def run():
    n = 220

    total = 0
    for a in range(2, 10000) :
        b = sum(sorted(factors(a))[:-1])
        n = sum(sorted(factors(b))[:-1])

        # print a, b, n
        if a == n and a != b:
            total += n

    print total






print timeit.timeit(run, number=1)



75 + 95 + 4
