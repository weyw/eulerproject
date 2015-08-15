'''
https://projecteuler.net/problem=9

= 23514624000
'''

import timeit
import math
import sys
from euler import *

def run():
    t = 1000
    a = 3
    b = 4
    c = 5

    count = 0
    found = False

    f = lambda x: x * x
    sq = map(f, range(0, t / 2 + 1))
    b = t // 2

    for a in range(1, t / 4):
        while not found :
            count += 1
            c = (sq[a] + sq[b]) ** 0.5
            d = a + b + c
            if d > t :
                b -= 1
            elif d == t :
                found = True
                break
            else :
                break
        if found :
            break

    print(a, b, c, a + b + c, a * b * c, count)



print timeit.timeit(run, number=1)
