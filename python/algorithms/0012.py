#!/usr/bin/env python3

from math import sqrt
from functools import reduce, lru_cache

# :: ---

@lru_cache(maxsize = None)
def triangle_number (x):
    return 1 if x == 1 else triangle_number(x - 1) + x

# :: https://stackoverflow.com/a/6800214
def factorize (n):
    return set(reduce(
        list.__add__,
        ( [i, n // i] for i in range(1, int(sqrt(n)) + 1) if n % i  == 0 )
    ))

def main ():
    n = 2

    while True:
        tn = triangle_number(n)
        factors = factorize(tn)

        if (len(factors) > 500):
            print(f'[{n}]: {tn} --- {len(factors)} divisors.')
            return

        n += 1

# :: ---
if __name__ == "__main__":
    main()
