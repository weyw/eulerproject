#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=22

=
'''

import timeit
import math
import sys
import datetime
from euler import *


def run():
    n = 220

    total = 0
    for a in range(2, 10000) :
        b = sum(sorted(factors(a))[:-1])
        n = sum(sorted(factors(b))[:-1])

        # print a, b, n
        if a == n and a != b:
            total += n

    print total






print timeit.timeit(run, number=1)



75 + 95 + 4
