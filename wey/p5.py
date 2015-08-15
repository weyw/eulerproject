# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# = 232792560

import timeit
import math
import sys
from euler import *

def run():

    # n = 10
    n = 20

    # 1, 2, 3,  4,  5,  6,   7,   8, 9, 10
    # 1, 2, 6, 12, 60, 60, 420, 840, 2520

    total = 1

    for i in range(2, n + 1):
        total = lcm(total, i)

    print(total)

print timeit.timeit(run, number=1)
