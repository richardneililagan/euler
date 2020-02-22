#!/usr/bin/env python3

from math import sqrt
from functools import lru_cache, reduce

# :: ---

primelist = None

def prime_generator (end):
    primes = [2]
    yield 2
    for x in range(3, end, 2):
        limit = int(sqrt(x))
        if all(x % p != 0 for p in primes if p <= limit):
            primes += [x]
            yield x

@lru_cache(maxsize = None)
def is_prime (n):
    if n < 2: return False
    if n % 2 == 0: return False
    if n in primelist: return True
    # :: ---
    limit = int(sqrt(n)) + 1
    for x in range(3, limit + 1, 2):
        if n % x == 0: return False
    return True

def is_valid_pair (x, y):
    _x, _y = str(x), str(y)
    return is_prime(int(_x + _y)) and is_prime(int(_y + _x))

@lru_cache(maxsize = None)
def prime_pairs (prime):
    pairs = (
        p for p in primelist
        if p > prime
        and is_valid_pair(prime, p)
    )
    return set(pairs)

def crawl (primes, target):
    pairs = map(lambda n: prime_pairs(n), primes)
    candidates = list(reduce(lambda a, v: a & v, pairs))

    if len(primes) == target - 1 and len(candidates) > 0:
        return (primes + [min(candidates)])

    if len(primes) == target - 1 and len(candidates) == 0:
        return None
    # :: ---
    for c in sorted(candidates):
        result = crawl(primes + [c], target)
        if result is not None:
            return result

    return None

def main (limit = 10000):
    global primelist
    primelist = set(p for p in prime_generator(limit))
    for p in sorted(primelist):
        primes = crawl([p], 5)
        if primes is not None:
            print(sum(primes), primes)
            return

# :: ---
if __name__ == "__main__":
    main(10000)
