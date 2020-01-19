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
    primes = [ x for x in range(2, 2000000) if is_prime(x) ]
    print(sum(primes))

# :: ---
if __name__ == "__main__":
    main()
