'''
https://projecteuler.net/problem=13

=
'''

import timeit
import math
import sys
from euler import *

def run():
    contents = []
    file_name = "p13.txt"
    total = 0;

    with open(file_name) as fp:
        for line in fp:
            contents.append(line[:11])

    for i in contents :
        total += int(i)

    print(contents)
    print(str(total)[:10])
    # print(sum(map(int, contents)))

    print()



print timeit.timeit(run, number=1)
