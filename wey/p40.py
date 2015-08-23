#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

= 210
in 0.157
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

d = "0"
p = 1
x = 1
c = 1

while len(d) < 1000002:
    d += str(x)
    if len(d) > c:
        p *= int(d[c])
        c *= 10
    x += 1

print p


# '''
print time.clock() - start_time


