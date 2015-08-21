#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=20
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

= 648
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
