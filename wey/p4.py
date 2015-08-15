# https://projecteuler.net/problem=4

# 906609

import timeit

def run():
    p = []

    for a in range(100, 1000):
        for b in range(100, 1000):
            c = str(a * b)
            left = c[:3]
            d = c[::-1]
            right = d[:3]

            if left == right:
                p.append(a * b)

    print(max(p))

print timeit.timeit(run, number=1)

