#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

= 443839
'''

import time
import math
import sys

from euler import *

start_time = time.clock()

total = 0

for a in range(10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(10) :
                for e in range(10) :
                    for f in range(10) :
                        l = [a, b, c, d, e, f]
                        sumd = sum(map(lambda x: x ** 5, l))
                        if sumd == int(''.join(map(str, l))) and sumd > 1:
                            # print sumd
                            total += sumd

print total
# '''
print time.clock() - start_time


