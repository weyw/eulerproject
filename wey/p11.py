'''
https://projecteuler.net/problem=11

=
'''

import timeit
import math
import sys
from euler import *

def run():

    contents = []
    avoid = []
    adder = []
    file_name = "p11.txt"
    size = 4

    max_nums = []
    max_total = 1



    with open(file_name) as fp:
        contents = [[int(x) for x in line.split()] for line in fp]

    # print(contents)
    # let's go across first
    for x in range(len(contents[0])) :
        for y in range(len(contents)) :
            cur = 1
            cur2 = 1

            if x < 16 :
                for i in range(4) :
                    cur *= contents[y][x + i]
                    if y < 16 :
                        cur2 *= contents[y + i][x + i]

                if cur2 > cur :
                    cur = cur2

                if cur > max_total :
                    max_total = cur


            cur = 1
            cur2 = 1
            if y < 16 :
                for i in range(4) :
                    cur *= contents[y + i][x]
                    if x > 3 :
                        cur2 *= contents[y + i][x - i]
                if cur2 > cur :
                    cur = cur2

                if cur > max_total :
                    max_total = cur



    print(max_total, max_nums)



print timeit.timeit(run, number=1)
