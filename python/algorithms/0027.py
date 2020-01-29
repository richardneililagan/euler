#!/usr/bin/env python3

from math import sqrt
from functools import lru_cache
from itertools import chain

# :: ---

@lru_cache(maxsize = None)
def is_prime (x):
    """Return a boolean specifying if x is a prime number."""
    if x <= 1:
        return False

    n = 2
    limit = sqrt(x) + 0.5

    while n <= limit:
        if (x % n == 0):
            return False

        n += 1

    return True

def prime_length (a, b):
    length = 0
    while True:
        x = qf(length, a, b)
        if not is_prime(x):
            return length

        length += 1

def qf (n, a, b):
    """Return the evaluation of the quadratic formula with given coefficients."""
    return (n ** 2) + (a * n) + b

def main ():
    candidate = (0, 0, 0)
    for a in range(-999, 1000):         # |a| < 1000
        for b in range(-1000, 1001):    # |b| <= 1000
            l = prime_length(a, b)
            if candidate[0]< l:
                candidate = (l, a, b)

    print(candidate[1] * candidate[2])

# :: ---
if __name__ == "__main__":
    main()
