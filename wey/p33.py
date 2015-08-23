#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

= 100
'''

import time
import math
import sys
from euler import *

from fractions import Fraction

start_time = time.clock()

top = 1
bottom = 1

for y in range(1, 10):
    for x in range(1, y + 1):
        if not x == y:
            for i in range(1, 10):
                if Fraction(int(str(x) + str(i)), int(str(i) + str(y))) == Fraction(x, y):
                    print str(x) + str(i), str(i) + str(y), x, y
                    top *= x
                    bottom *= y

print Fraction(top, bottom)
# '''
print time.clock() - start_time


