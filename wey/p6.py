'''
https://projecteuler.net/problem=6

= 25164150
'''

import timeit
import math
import sys
from euler import *

def run():

    # n = 10
    n = 100

    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
    sum_of_numbers = (n * (n + 1)) / 2

    total = sum_of_numbers ** 2 - sum_of_squares

    print(total)

print timeit.timeit(run, number=1)
