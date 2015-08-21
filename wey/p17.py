'''
https://projecteuler.net/problem=18

= 21124
'''

import timeit
import math
import sys
from euler import *

def get_num(n) :
    words = {0: 0,
             1: 3,
             2: 3,
             3: 5,
             4: 4,
             5: 4,
             6: 3,
             7: 5,
             8: 5,
             9: 4,
             10: 3,
             11: 6,
             12: 6,
             13: 8,
             14: 8,
             15: 7,
             16: 7,
             17: 9,
             18: 8,
             19: 8,
             20: 6,
             30: 6,
             40: 5,
             50: 5,
             60: 5,
             70: 7,
             80: 6,
             90: 5,
             100: 7,
             1000: 8
             }

    result = 0
    thousands = 0
    hundreds = 0
    tens = 0
    ones = 0

    if len(n) == 4 :
        thousands = math.floor(n / 1000)
        t = n - thousands * 1000
        hundreds = math.floor(t / 100)
        t -= hundreds * 100
        tens = math.floor(t / 10)
        t -= tens * 10
        ones = math.floor(t)

        result += 3 + words[1000]
    elif len(n) == 3 :
        hundreds = math.floor(t / 100)
        t = n - hundreds * 100
        tens = math.floor(t / 10)
        t -= tens * 10
        ones = math.floor(t)

        result += 3 + words[100]
    elif len(n) == 2 :
        if n <= 20 :
            result += words[n]
        else :
            tens = math.floor(t / 10)
            t = n - tens * 10
            ones = math.floor(t)

    result += words[thousands]



def run():

    total = 0
    for i in range(1000 + 1) :
        total += get_num(i)

    print (q, sum(map(int, q)))




print timeit.timeit(run, number=1)



