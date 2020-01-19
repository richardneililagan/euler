#!/usr/bin/env python3

from math import sqrt

# :: ---

def is_prime (x):
    n = 2
    limit = sqrt(x)

    while n <= limit:
        if (x % n == 0):
            return False

        n += 1

    return True

def main ():
    i = 0
    n = 2

    while i <= 10001:
        if is_prime(n):
            i += 1

        if i == 10001:
            print(n)
            return

        n += 1

# :: ---
if __name__ == "__main__":
    main()
