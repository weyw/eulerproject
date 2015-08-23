#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

=
'''

import time
import math
import sys
from euler import *

def is_palindromic(n):
    a = str(n)
    p = len(a)
    if p % 2 == 0:
        p = p / 2
    else:
        p = p // 2 + 1

    left = a[:p]
    right = a[-1 * p:]
    if left != right[::-1]:
        return False

    b = bin(n)[2:]
    p = len(b)
    if p % 2 == 0:
        p = p / 2
    else:
        p = p // 2 + 1

    left = b[:p]
    right = b[-1 * p:]
    if left != right[::-1]:
        return False

    return True

start_time = time.clock()
''' '''
n = 1000000
n = 1000

total = 0

for i in range(1, 1000000):
    if is_palindromic(i):
        total += i

print total



# '''
print time.clock() - start_time


