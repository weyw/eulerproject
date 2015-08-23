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



p = [0] * 1000

for i in range(1, 1000, 2):
    for z in range(i + 1, 1000):
        n = 4 * z ** 2 + 2 * z * i;
        if n > 999:
            break
        for m in range(n, 1000, n):
            if m > 999:
                break
            p[m] += 1

for i in range(1000):
    if p[i] > max_count:
        max_count = p[i]
        max_p = i



# import itertools, math
# N = 1000
# nsol = [0]*N
# for a in xrange(1, N-N/2):
#     for b in itertools.count(a+1):
#         c_squared = a*a + b*b
#         c = int( math.sqrt( c_squared))
#         p = a + b + c
#         if not p < N: break
#         if c*c == c_squared:
#             nsol[p] += 1
# print nsol.index( max( nsol))


# for p in range(2, 1000, 2):
#     count = 0
#     for a in range(p / 4):
#         for b in range(a + 1, (p - a) / 2):
#             if a + b + math.sqrt(a ** 2 + b **2) == p:
#                 count += 1

#     if count > max_count:
#         max_count = count
#         max_p = p

print max_count, max_p

# '''
print time.clock() - start_time


