#!/usr/bin/env python3

from math import sqrt

# :: ---

def is_triangular (n):
    i = (sqrt(8 * n + 1) - 1) / 2
    return i.is_integer()

def is_pentagonal (n):
    i = (1 + sqrt(24 * n + 1)) / 6
    return i.is_integer()

def hexagonal_generator (start):
    n = start
    while True:
        yield n * (2 * n - 1)
        n += 1

def main ():
    g = hexagonal_generator(144)
    n = 2

    while not is_triangular(n) or not is_pentagonal(n):
        n = next(g)

    print(n)

# :: ---
if __name__ == "__main__":
    main()
