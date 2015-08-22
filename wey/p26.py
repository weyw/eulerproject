#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=27



=
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
# print str(divide(1, 3))[3:-1]

d = 1000
# d = 10

x_max = 0
d_max = 0

for i in range(2, d):
    x = str(divide(1, i))

    try:
        start = x.index("[")
        y = len(x[start:-2])
        if y > x_max :
            x_max = y
            d_max = i

    except:
        pass

print d_max, x_max


# '''
print time.clock() - start_time


