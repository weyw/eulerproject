#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

=296962999629
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

prime_set = prime_sieve(10000)
found = []


for n in range(1001, 3340, 2):
    if n in set([1487, 4817, 8147]):
        continue

    if n in prime_set:
        perms = map(int, permute(str(n)))
        if n + 3330 in perms and n + 6660 in perms and n + 3330 in prime_set and n + 6660 in prime_set:
            print n
            found.append(n)
            found.append(n + 3330)
            found.append(n + 6660)



# for n in range(1001, 10000, 2):
#     if n in set([1487, 4817, 8147]):
#         continue

#     if n in prime_set:
#         perms = map(int, sorted(permute(str(n))))
#         n_pos = perms.index(n)

#         for p in perms[n_pos - 1:]:
#             if p not in prime_set and p <= n:
#                 continue

#             p_pos = perms.index(p)

#             for q in perms[p_pos - 1:]:
#                 if q not in prime_set and q <= p:
#                     continue

#                 if q - p == p - n and p - n != 0:
#                     print n, p, q
#                     found.append(n)
#                     found.append(p)
#                     found.append(q)

# sorted(found)
print str(found[0]) + str(found[1]) + str(found[2])








# '''
print time.clock() - start_time


