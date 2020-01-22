#!/usr/bin/env python3

from math import sqrt
from functools import reduce

# :: ---

# :: https://stackoverflow.com/a/6800214
def get_proper_divisors (n):
    s = set(reduce(
        list.__add__,
        (
            [i, n // i]
            for i in range(1, int(sqrt(n)) + 1)
            if n % i == 0
        )
    ))

    return set([ x for x in s if x != n ])

def main ():
    pairs = [ 
        (x, sum(get_proper_divisors(x)))
        for x in range(1, 10000)
    ]

    amicables = [
        p for p in pairs
        if p[0] < p[1]
        and p[1] < len(pairs)
        and pairs[p[1] - 1][1] == p[0]
    ]

    total = sum(map(lambda p: sum(p), amicables))
    print(total)

# :: ---
if __name__ == "__main__":
    main()
