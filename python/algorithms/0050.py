#!/usr/bin/env python3

from functools import lru_cache
from math import sqrt

# :: ---

LIMIT = 1000000

@lru_cache(maxsize = None)
def is_prime (n):
    if n < 2: return False
    limit = int(sqrt(n) + 0.5)
    for d in range(2, limit + 1):
        if n % d == 0: return False
    return True

def get_max_length (primes, max_sum = LIMIT):
    for x in range(2, len(primes)):
        if sum(primes[0:x]) >= max_sum: return x - 1
    return len(primes)

def main ():
    primes = [ x for x in range(1, LIMIT) if is_prime(x) ]
    max_length = get_max_length(primes)

    for length in list(range(21, max_length))[::-1]:
        for i in range(0, len(primes) - length):
            s = sum(primes[i:i + length])
            if s >= LIMIT: break           # :: shortcircuit
            if is_prime(s):
                print(s, length)
                return

# :: ---
if __name__ == "__main__":
    main()
