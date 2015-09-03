#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

= 153
'''

import time
import math
import sys
import string
from euler import *

start_time = time.clock()
''' '''
from fractions import Fraction
from decimal import *

tot = 0
top = 3
bot = 2

for i in range(1000):
    if int(math.log10(top)) > int(math.log10(bot)):
        tot += 1
    bot, top = top + bot, 2 * bot + top

print tot


# '''
print time.clock() - start_time


