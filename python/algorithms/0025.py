#!/usr/bin/env python3

from functools import lru_cache

# :: ---

@lru_cache(maxsize = None)
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main ():
    n = 1
    f = fibonacci(n)

    while len(list(str(f))) < 1000:
        n += 1
        f = fibonacci(n)

    print(n)

# :: ---
if __name__ == "__main__":
    main()
