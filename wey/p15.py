'''
https://projecteuler.net/problem=15

=
'''

import timeit
import math
import sys
from euler import *




def run():
    cube_size = 20

    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    print L[cube_size - 1]




print timeit.timeit(run, number=1)



