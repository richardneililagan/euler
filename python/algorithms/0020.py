#!/usr/bin/env python3

from functools import lru_cache

# :: ---

@lru_cache(maxsize=None)
def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main ():
    total = sum([ int(x) for x in str(factorial(100)) ])
    print(total)

# :: ---
if __name__ == "__main__":
    main()
