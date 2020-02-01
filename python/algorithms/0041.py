#!/usr/bin/env python3

from functools import lru_cache
from itertools import permutations
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

def generator (length = 9):
    d = set(str(123456789)[0:length])
    c = permutations(d, length)
    for x in c:
        yield int("".join(x)) 

def main ():
    cur_length = 9

    while cur_length > 0:
        g = generator(cur_length)
        c = [ x for x in g if is_prime(x) ]

        if len(c) > 0:
            print(max(c))
            return

        cur_length -= 1

# :: ---
if __name__ == "__main__":
    main()
