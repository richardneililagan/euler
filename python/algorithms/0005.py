#!/usr/bin/env python3

from math import sqrt
from functools import reduce
from collections import Counter

# :: ---

def factorize (x, a):
    n = 2
    limit = sqrt(x)

    while n <= limit:
        if (x % n == 0):
            factorize(n ,a)
            factorize(int(x / n), a)
            return

        n += 1

    a.append(x)

def mapper (x):
    l = []
    factorize(x, l)
    return Counter(l)

def max_digits_occurrence_reducer (a, c):
    for digit in c:
        current_count = a[digit]
        if c[digit] > current_count:
            a[digit] = c[digit]

    return a

def main ():
    counts = map(mapper, range(1, 21))
    init_dict = dict(map(lambda x: (x, 0), range(1, 21)))
    max_digits = reduce(max_digits_occurrence_reducer, counts, init_dict)

    total = reduce(
        lambda a, v: a * (v ** max_digits[v]),
        max_digits.keys(),
        1
    )

    print(max_digits)
    print(total)

# :: ---
if __name__ == "__main__":
    main()
