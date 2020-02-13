#!/usr/bin/env python3

from functools import lru_cache

# :: ---

LIMIT = 100

@lru_cache(maxsize = None)
def factorial (n):
    return 1 if n <= 1 else n * factorial(n - 1)

def generator (limit = LIMIT):
    for n in range(1, limit + 1):       # :: inclusive
        for r in range(1, n + 1):       # :: inclusive
            yield factorial(n) / (factorial(n - r) * factorial(r))

def main ():
    g = generator()
    print(len([ x for x in g if x > 1000000 ]))

# :: ---
if __name__ == "__main__":
    main()
