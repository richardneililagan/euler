#!/usr/bin/env python3

from math import sqrt
from collections import Counter

# :: ---

def is_int (n):
    return n == int(n)

def p_generator (p_max):
    for a in range(1, p_max - 1):
        for b in range(1, p_max - a - 1):
            c = sqrt(a ** 2 + b ** 2)
            if (is_int(c)):
                yield int(a + b + c), a, b, c

def main ():
    p = Counter([ P for P, a, b, c in p_generator(1000) if P <= 1000 ])
    print(p.most_common(1)[0][0])

# :: ---
if __name__ == "__main__":
    main()
