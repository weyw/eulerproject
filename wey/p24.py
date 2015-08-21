#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

= 2783915460
'''

import timeit
import math
import sys
import datetime
import itertools
from euler import *

def run():
    p = list(itertools.permutations("0123456789"))
    total = ""
    n = 1000000 - 1
    for i in p[n]:
        total += i
    print total, p[n]



# '''
print timeit.timeit(run, number=1)


