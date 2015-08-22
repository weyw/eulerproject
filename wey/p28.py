#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

= 669171001
'''

import time
import math
import sys
from euler import *

start_time = time.clock()

n = 1001
# n = 5

total = 1
for i in range(3, n + 1, 2):
    total += 4 * i ** 2 - 6 * i + 6

print total
# '''
print time.clock() - start_time


