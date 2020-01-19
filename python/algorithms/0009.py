#!/usr/bin/env python3

from math import floor

# :: ---

def algorithm (n):
    for a in range(1, floor(n / 3)):
        for b in range(a, floor((n - a) / 2) + 1):
            c = 1000 - (a + b)
            if ((a ** 2) + (b ** 2)) == (c ** 2):
                return (a * b * c)

def main ():
    print(algorithm(1000))

# :: ---
if __name__ == "__main__":
    main()
