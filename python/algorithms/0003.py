#!/usr/bin/env python3

from math import sqrt
from itertools import chain

# :: ---

def factorize (x, a):
    n = 2
    limit = sqrt(x)

    while n < limit:
        if (x % n == 0):
            factorize(n, a)
            factorize(int(x / n), a)
            return

        n += 1

    a.append(x)

def main ():
    l = []
    factorize(600851475143, l)
    l.sort(reverse = True)
    print(l[0])

# :: ---
if __name__ == "__main__":
    main()
