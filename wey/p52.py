#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

= 142857
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''

for x in range(123456, 1000000):
    s = "".join(sorted(list(str(x))))

    # found = True
    # for i in range(2, 7):
    #     if s != "".join(sorted(list(str(x * i)))):
    #         found = False
    #         break
    # if found:
    #     print x
    #     break


    if (s == "".join(sorted(list(str(x * 2))))) and (s == "".join(sorted(list(str(x * 3))))) and (s == "".join(sorted(list(str(x * 4))))) and (s == "".join(sorted(list(str(x * 5))))) and (s == "".join(sorted(list(str(x * 6))))):

        print x
        break

# '''
print time.clock() - start_time


