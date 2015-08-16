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

def run():
    n = 13
    max_chain = 0
    cur_chain = 0
    cur_starting_num = 3
    max_starting_num = 0

    for cur_starting_num in range(3, 1000000) :
        n = cur_starting_num
        cur_chain = 0

        while n > 1 :
            cur_chain += 1
            if cur_chain > max_chain :
                max_chain = cur_chain
                max_starting_num = cur_starting_num
            n = collatz(n)

    print(max_starting_num, max_chain)


print timeit.timeit(run, number=1)
