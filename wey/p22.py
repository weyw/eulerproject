#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

=
'''

import timeit
import math
import sys
import datetime
from euler import *


def run():
    file_name = "p022_names.txt"
    names = []
    with open(file_name) as f:
        for line in f:
            names = line.split(",")
    #'''

    names.sort()
    place = 1
    total = 0
    for n in names :
        worth = 0

        print n
        for letter in list(n):
            if ord(letter) != ord('"'):
                worth += (ord(letter) - 64)
        total += place * worth
        place += 1

    print total


# '''
print timeit.timeit(run, number=1)


