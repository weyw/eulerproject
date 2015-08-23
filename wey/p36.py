#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

= 872187
'''

import time
import math
import sys
from euler import *



start_time = time.clock()
''' '''
n = 1000000
n = 1000

total = 0

for i in range(1, 1000000, 2):
    if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
        total += i

print total



# '''
print time.clock() - start_time


