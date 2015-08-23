#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

= 45228
'''

import time
import math
import sys

from euler import *

start_time = time.clock()

total = 0
all_products = set()

for x in range(2, 60):
    xs = str(x)

    if len(xs) > 1 :
        if xs[:1] == xs[-1:] or xs[-1:] == "0":
            continue

    start = 1234 if x < 10 else 123
    for y in range(start, 10000 // x):
        p = x * y
        n = str(x) + str(y) + str(p)
        if "".join(sorted(n)) == '123456789' and len(n) == 9 :
            # print x, y, p
            all_products.add(p)

print sum(all_products)

# '''
print time.clock() - start_time


