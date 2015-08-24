#!/usr/bin/python
# -*- coding: utf-8 -*-

from euler import *

n = 1159

for j in range(4):
    print n + j, set(prime_factors(n + j))
    # if len(set(prime_factors(n + j))) != 4:


print len(set(prime_factors(n)))
