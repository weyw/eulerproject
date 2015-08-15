# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143
# 6857

import timeit
import math
import sys

def is_prime(m):
    primes = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if m in primes :
        return True

    f = 5
    while f <= math.floor(math.sqrt(m)) :
        if m % f == 0 or m % (f + 2) == 0: return False
        f += 6
    return True



prime_factors = []

def run():
    n = 600851475143
    # n = 13195
    # n = 408464633

    # let's try 2 first
    d = 2
    while n % d == 0 :
        prime_factors.append(d)
        n /= d

    # now 3
    d = 3
    while d <= n:
        if is_prime(d) :
            while n % d == 0 :
                print(n)
                prime_factors.append(d)
                n /= d
        d += 2

    print("The prime factors are: ", prime_factors)
    print("The largest prime factor is: ", max(prime_factors))

print(timeit.timeit(run, number=1))
