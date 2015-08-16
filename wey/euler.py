import math
import numpy

def is_prime(m):
    ''' returns True if "m" is prime '''

    primes = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if m in primes :
        return True

    if not m % 2 or not m % 3 or not m % 5:
        return False

    f = 5
    while f <= math.floor(math.sqrt(m)) :
        if m % f == 0 or m % (f + 2) == 0: return False
        f += 6
    return True


def prime_factors(n):
    ''' return of list of "n's" prime factors '''

    factors = []
    d = 2
    while n % d == 0 :
        factors.append(d)
        n /= d

    # now 3
    d = 3
    while d <= n:
        if is_prime(d) :
            while n % d == 0 :
                print(n)
                factors.append(d)
                n /= d
        d += 2

    return factors


def gcd(x, y):
    ''' return greatest common divisor using Euclid's algorithm '''

    while y:
        x, y = y, x % y

    return x

def lcm(x, y):
    ''' return lowest common multiple of "x" and "y" '''

    return (x * y) // gcd(x, y)


def prime_sieve2(n):

    primes = [True] * (n + 1)

    primes[0] = False
    primes[1] = False

    for i in range(4, n):
        if primes[i]:
            if i % 2 == 0 or i % 3 == 0 :
                primes[i] = False
                continue

            j = i * i
            while j < n + 1:
                primes[j] = False
                j += i

    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)

    return result

def prime_sieve(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """

    if n < 6 :
        primes = [2, 3, 5, 7, 13, 17]
        return primes[:n]

    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def factors(n) :
    ''' return all factors for n '''

    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(math.floor(math.sqrt(n))) + 1) if n % i == 0)))
