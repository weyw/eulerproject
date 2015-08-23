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

for y in range(12, 100):
    for x in range(11, y + 1):
        if not (str(x)[1] == "0" or str(y)[1] == "0" or str(x)[0] == str(y)[0] or str(x)[1] == str(y)[1]) :
            if str(x)[1] == str(y)[0]:
                if Fraction(x, y) == Fraction(int(str(x)[0]), int(str(y)[1])):
                    print x, y, int(str(x)[0]), int(str(y)[1])
                    top *= int(str(x)[0])
                    bottom *= int(str(y)[1])
            if str(x)[0] == str(y)[1]:
                if Fraction(x, y) == Fraction(int(str(x)[1]), int(str(y)[0])):
                    print x, y, int(str(x)[1]), int(str(y)[0])
                    top *= int(str(x)[1])
                    bottom *= int(str(y)[0])

print Fraction(top, bottom)
# '''
print time.clock() - start_time


