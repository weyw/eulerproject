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

=
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

count = 0
for i in range(1000):
    n = Fraction(2) + Fraction(0.5)
    if i == 0:
        n = Fraction(2)
    elif i == 1:
        pass
    else:
        for j in range(1, i):
            n = Fraction(2) + Fraction(1) / n

    n = Fraction(1 + Fraction(1) / n)
    # print n
    if len(str(n.numerator)) > len(str(n.denominator)):
        count += 1

print count


# '''
print time.clock() - start_time


