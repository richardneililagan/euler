#!/usr/bin/env python3

from functools import lru_cache

# :: ---

@lru_cache(maxsize = None)
def pn (n):
    """
    P(n) = 2 + (1 / P(n - 1))
    where P(1) = 2

    returns (a, b) where a, b is (a / b) in fractional form
    """
    if n <= 1: return (2, 1)
    # :: ---

    a, b = pn(n - 1)
    return b + 2 * a, a

def generator (end):
    for n in range(end):
        a, b = pn(n)
        yield b + a, a

def main ():
    g = generator(1000)
    print(sum(1 for a, b in g if len(str(a)) > len(str(b))))

# :: ---
if __name__ == "__main__":
    main()
