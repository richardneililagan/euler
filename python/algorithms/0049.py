#!/usr/bin/env python3

from itertools import permutations
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

def get_candidates (x):
    digits = list(str(x))
    pn = [ int("".join(p)) for p in permutations(digits, len(digits)) ]
    return [ n for n in pn if n > x and is_prime(n) ]

def generator ():
    x = 1000

    while x < 10000:
        x += 1
        if not is_prime(x): continue
        c = get_candidates(x)
        for y in c:
            d = y - x
            z = y + d
            if z in c:
                yield x, y, z

def main ():
    g = generator()
    s = set([ str(x) + str(y) + str(z) for x, y, z in g ])

    [ print(a) for a in s ]

# :: ---
if __name__ == "__main__":
    main()
