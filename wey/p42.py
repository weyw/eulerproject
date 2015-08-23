#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

= 162
in
'''

import time
import math
import sys
from euler import *

start_time = time.clock()
''' '''

n = 0
words = set()
triangle_words = set()
found = set()
file_name = "p42_words.txt"

with open(file_name) as f:
    for line in f:
        words = line.replace('\"', '').split(",")

for n in range(250):
    triangle_words.add(n * (n + 1) / 2)

for w in words:
    v = 0
    for i in list(w):
        v += ord(i) - 64

    if v in triangle_words:
        found.add(w)

print len(found)

# '''
print time.clock() - start_time


