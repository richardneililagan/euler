#!/usr/bin/env python3

from functools import lru_cache
from math import sqrt

# :: ---

@lru_cache(maxsize = None)
def is_prime (n):
    if n < 2: return False

    limit = int(sqrt(n) + 0.5)
    for d in range(2, limit + 1):
        if n % d == 0: return False

    return True

def is_perfect_square (n):
    return sqrt(n).is_integer()

def odd_composite_generator ():
    n = 7
    while True:
        if not is_prime(n):
            yield n
        n += 2

def main ():
    g = odd_composite_generator()
    while True:
        n = next(g)
        primes = [ x for x in range(2, n) if is_prime(x) ]
        addends = map(lambda p: is_perfect_square((n - p) / 2), primes)

        if not any(addends):
            print(n)
            break

# :: ---
if __name__ == "__main__":
    main()
