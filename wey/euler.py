import math
import numpy
import random

def is_prime(m):
    ''' returns True if "m" is prime '''

    if m > 20051686:
        return MillerRabinPrimalityTest(m)
    if m <= 1 :
        return False
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

def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False

    ''' first we want to express n as : 2^s * r ( were r is odd ) '''

    ''' the odd part of the number '''
    oddPartOfNumber = number - 1

    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0

    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1

    '''
    since there are number that are cases of "strong liar" we
    need to check more then one number
    '''
    for time in range(3):

        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break

        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)

        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1

            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)

                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False

    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True

def prime_factors(n):
    ''' return of list of "n's" prime factors '''

    primes_set = set(prime_sieve(n))
    factors = []
    d = 2
    while n % d == 0 :
        factors.append(d)
        n /= d

    # now 3
    d = 3
    while d <= n:
        if d in primes_set :
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
    ''' return a sorted list of all factors for n '''

    return sorted(reduce(list.__add__, ([i, n // i] for i in range(1, int(math.floor(math.sqrt(n))) + 1) if n % i == 0)))

def divide(numerator, denominator, detect_repetition=True, digit_limit=None):

    # If repetition detection is off, you must
    # specify a limit on the digits returned
    if not detect_repetition and digit_limit == None:
        return None

    decimal_found = False

    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)

    if numerator == 0:
        return answer

    answer += '.'

    # Maintain a list of all the intermediate numerators
    # and the length of the output at the point where that
    # numerator was encountered. If you encounter the same
    # numerator again, then the decimal repeats itself from
    # the last index that numerator was encountered at.
    states = {}

    while numerator > 0 and (digit_limit == None or digit_limit > 0):

        if detect_repetition:
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return non_repeating + '[' + repeating + ']'
            states[numerator] = len(answer)

        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1

    if numerator > 0:
        return answer + '...'
    return answer

def permute(s):
    ''' return a list of permutations of string s '''

    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                res += [c + perm]

    return res
