#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

= 840
in 90.34
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

max_count = 0
max_p = 0
for p in range(120, 1000):
    count = 0
    for a in range(1, p):
        for b in range(1, p - a):
            c = math.sqrt(a ** 2 + b ** 2)

            if a + b + c == p:
                count += 1

    if count > max_count:
        max_count = count
        max_p = p

print max_count, max_p

# '''
print time.clock() - start_time


