#!/usr/bin/env python3

from functools import lru_cache
from math import sqrt

# :: ---

@lru_cache(maxsize = None)
def is_prime (n):
    if n < 2:
        return False

    limit = int(sqrt(n) + 0.5)

    for d in range(2, limit + 1):
        if n % d == 0:
            return False

    return True

def truncate (n):
    lt = [ int(str(n)[x::]) for x in range(1, len(str(n))) ]
    rt = [ int(str(n)[0:x]) for x in range(1, len(str(n))) ]

    return rt + [n] + lt

def prime_generator ():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def main ():
    g = prime_generator()
    tprimes = set()

    while len(tprimes) < 11:
        n = next(g)
        if (n < 10):
            continue

        if all(map(lambda x: is_prime(x), truncate(n))):
            tprimes.add(n)

        n += 1

    print(sum(tprimes))

# :: ---
if __name__ == "__main__":
    main()
