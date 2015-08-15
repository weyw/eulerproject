# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# = 233168

import sys

def sum(n):
    total = 0

    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i

    return total

n = 20

if len(sys.argv) == 2:
    n = int(sys.argv[1])


print(sum(n))
