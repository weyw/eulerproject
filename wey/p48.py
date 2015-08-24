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
d10 = ""
count = 0
for n in range(1, 1000):
    t += n ** n

    # if len(str(t)) > 11:
    #     if d10 != str(t)[-10]:
    #         d10 = str(t)[-10]
    #         count = 0
    #     else:
    #         if count > 4:
    #             break
    #         else:
    #             count += 1

print str(t)[-10:]






# '''
print time.clock() - start_time


