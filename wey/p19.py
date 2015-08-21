'''
https://projecteuler.net/problem=19

= 171
'''

import timeit
import math
import sys
import datetime
from euler import *


def run():
    date_start = 19010101
    date_end = 20001231

    sundays = 0

    for y in range(1901, 2001) :
        for m in range(1, 13) :
            if datetime.date(y, m, 1).weekday() == 6 :
                sundays += 1

    print (sundays)







print timeit.timeit(run, number=1)



75 + 95 + 4
