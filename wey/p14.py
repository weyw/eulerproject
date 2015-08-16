'''
https://projecteuler.net/problem=14

= 837799
'''

import timeit
import math
import sys
from euler import *

def collatz(n):
    if n % 2 == 0 :
        return n /2
    else:
        return 3 * n + 1

class ChainCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(collatz(n))
            self.cache[n] = c + 1
            return c + 1

def run():

    chainlen = ChainCache()
    n = 1000000

    m = 0
    v = 0
    for i in range(1, n):
        l = chainlen(i)
        if l > m:
            m = l
            v = i
    print(v, m)



print timeit.timeit(run, number=1)
