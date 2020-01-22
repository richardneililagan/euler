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

def is_abundant (n):
    divisors = get_proper_divisors(n)
    return n < sum(divisors)

def main ():
    limit = 28124

    abundants = [ x for x in range(1, limit) if is_abundant(x) ]
    abundant_sums = reduce(
        lambda a, v: a.union([
            v + x
            for x in abundants
            if v <= x < (limit - v)
        ]),
        abundants,
        set()
    )

    difference = set(range(1, limit)).symmetric_difference(abundant_sums)

    print(sum(difference))

# :: ---
if __name__ == "__main__":
    main()
