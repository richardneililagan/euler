#!/usr/bin/env python3

from math import sqrt
from functools import lru_cache

# :: ---

@lru_cache(maxsize = None)
def pfactorize (x):
    n = 2
    a = []
    limit = sqrt(x)

    while n <= limit:
        if (x % n == 0):
            a += pfactorize(n)
            a += pfactorize(int(x / n))
            return a
        n += 1

    return [x]

def pfactor_length_generator (length):
    n = 2
    while True:
        spf = [ set(pfactorize(x)) for x in range(n, n + length) ]
        lspf = map(lambda s: len(s) == length, spf)
        if (all(lspf)):
            yield n

        n += 1

def main ():
    g = pfactor_length_generator(4)
    print(next(g))

# :: ---
if __name__ == "__main__":
    main()
