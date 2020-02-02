#!/usr/bin/env python3

from math import sqrt

# :: ---

def pn (n):
    return (n * ((3 * n) - 1)) // 2

def is_pn (n):
    """
    P(n) = n(3n - 1) / 2
    => 2P(n) = n(3n - 1)
    => 2P(n) = 3n^2 - n
    => 24P(n) = 36n^2 - 12n
    => 24P(n) = 36n^2 - 12n + 1 - 1
    => 24P(n) = (6n - 1)^2 - 1
    => 24P(n) + 1 = (6n - 1)^2
    => sqrt(24P(n) + 1) = 6n - 1
    => 6n = 1 + sqrt(24P(n) + 1)
    => [QED] n = (1 + sqrt(24P(n) + 1)) / 6
    """
    return (1 + sqrt(24 * n + 1))  % 6 == 0

def main ():
    print(is_pn(51))

# :: ---
if __name__ == "__main__":
    main()
