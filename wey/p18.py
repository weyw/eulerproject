'''
https://projecteuler.net/problem=18

= 1074
'''

import timeit
import math
import sys
from euler import *


def run():
    file_name = "p18.txt"
    # read in the data
    rows = []
    with open(file_name) as f:
        for line in f:
            rows.append([int(i) for i in line.rstrip('\n').split(" ")])

    height = len(rows)
    i = height - 2
    while i >= 0 :
        for j in range(len(rows[i])) :
            rows[i][j] += max(rows[i + 1][j], rows[i + 1][j + 1])

        i -= 1

    print rows[0][0]






print timeit.timeit(run, number=1)



75 + 95 + 4
