#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

= 9110846700
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

t = 0
for n in range(1, 1000):
    t += n ** n

print str(t)[-10:]






# '''
print time.clock() - start_time


