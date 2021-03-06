#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

= 1533776805
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

def is_pent(t):
    # print x
    if ((24 * t + 1) ** 0.5) % 6 == 5.0:
        return True
    return False

def is_hex(t):
    # print n
    if (math.sqrt(8 * t + 1) + 1) % 4 == 0.0:
        return True
    return False

l = 286
u = 60000
for n in range(l, u):
    t = n * (n + 1) / 2
    if is_pent(t) and is_hex(t):
        print n, (t)
        break


# '''
print time.clock() - start_time


