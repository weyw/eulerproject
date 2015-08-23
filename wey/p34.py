#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

= 40730
'''

import time
import math
import sys
from euler import *
start_time = time.clock()
'''
'''
m = 10
n = math.factorial(m)
# n = 10
total = []

for i in range(3, n + 1):
    s = 0
    for j in list(str(i)):
        s += math.factorial(int(j))

    if s == i:
        total.append(i)

print total, sum(total)
# '''
print time.clock() - start_time


