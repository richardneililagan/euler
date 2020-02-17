#!/usr/bin/env python3

from math import sqrt
from functools import lru_cache

# :: ---

@lru_cache(maxsize = None)
def is_prime (n):
    if n < 2:
        return False
    # :: ---
    limit = int(sqrt(n) + 0.5)
    return next((x for x in range(2, limit + 1) if n % x == 0), 0) == 0

def generator ():
    side_length = 1
    candidate_count = 1
    primes_count = 0

    while True:
        side_length += 2
        base = side_length ** 2
        d = side_length - 1
        candidates = [ base - (x * d) for x in range(1, 4) ]
        primes_count += sum(1 for x in candidates if is_prime(x))
        candidate_count += 4

        yield primes_count, candidate_count, side_length

def main ():
    g = generator()
    print(next(s for (p, c, s) in g if (p / c < 0.10)))

# :: ---
if __name__ == "__main__":
    main()
