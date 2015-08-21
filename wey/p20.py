#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=21


=
'''

import timeit
import math
import sys
import datetime
from euler import *


def run():
    # n = 10
    n = 100

    product = math.factorial(n)

    # print list(str(product))
    print (sum(map(int, list(str(product)))))







print timeit.timeit(run, number=1)



75 + 95 + 4
