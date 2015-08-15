import math

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


def prime_sieve(n):
    ''' returns a list of "n" primes '''

    if n == 1:
        return [2]
    if n == 2:
        return [2, 3]
    elif (n - 2)
    primes = [5, 7, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
              89, 97]
