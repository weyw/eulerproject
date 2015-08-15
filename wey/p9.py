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

    while c < 500 or not found:
        for a in range(4, 500):
            for b in range(5, 500):
                count += 1

                c = math.sqrt(a ** 2 + b ** 2)
                if math.floor(c) == c:
                    if a + b + c == 1000:
                        found = True
                        break

            if found:
                break

        if found:
            break

    print(a, b, c, a + b + c, a * b * c, count)



print timeit.timeit(run, number=1)
