#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=32

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

= 73682
'''

import time
import math
import sys

from euler import *

start_time = time.clock()

t = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = [1] + [0] * t


for c in coins :
    for i in range(c, t + 1):
        total[i] += total[i - c]

print total[t]
# '''
print time.clock() - start_time


