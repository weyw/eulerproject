#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

= 443839
'''

import time
import math
import sys

from euler import *

start_time = time.clock()

c=0
for q in range (10):
  for w in range (q + 1):
    for e in range (w + 1):
      for r in range (e + 1):
         for t in range (r + 1):
            for y in range (t + 1):
                v= (q**5 + w**5+e**5+r**5+t**5+y**5)

                b=0
                n=str(v)
                m=0
                while m < len(n) and b <= v:
                       b+=int(n[m])**5
                       m+=1
                if b == v :
                      c += v
print c-1

# '''
print time.clock() - start_time


