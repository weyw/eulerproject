#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=56

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

= 972
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''

max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        x = a ** b
        n = sum(map(int, list(str(x))))

        if n > max_sum :
            max_sum = n

print max_sum

# '''
print time.clock() - start_time


