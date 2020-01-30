#!/usr/bin/env python3

from functools import lru_cache
from math import sqrt

# :: ---

MAX_LIMIT = 1000000

@lru_cache(maxsize = None)
def is_prime (n):
    limit = int(sqrt(n) + 0.5)

    for d in range(2, limit + 1):
        if n % d == 0:
            return False

    return True

def cycle (n):
    digits = list(str(n))
    yield n

    d = digits[1::] + digits[0:1]
    dn = int("".join(d))
    while dn != n:
        yield dn
        d = d[1::] + d[0:1]
        dn = int("".join(d))

def main ():
    checked = set()
    cyclicals = set()

    for n in range(2, MAX_LIMIT):
        if n in checked: continue

        a = [ x for x in cycle(n) ]
        is_cyclical = all(map(lambda x: is_prime(x), a))

        checked.update(a)
        if is_cyclical: cyclicals.update(a)

    print(len(cyclicals))

# :: ---
if __name__ == "__main__":
    main()
