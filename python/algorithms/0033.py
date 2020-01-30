#!/usr/bin/env python3

from functools import reduce
from math import sqrt

# :: ---

def shares_digit (m, n):
    sm = list(str(m))
    sn = list(str(n))
    sd = set(sm) & set(sn)

    if len(sd) == 1 and "0" not in sd:
        d = list(sd)[0]
        nm = "".join([ x for x in sm if int(x) != int(d) ])
        nn = "".join([ x for x in sn if int(x) != int(d) ])

        if len(nm) == 0 or len(nn) == 0 or nm >= nn:
            return False, 0, 0
        else:
            return True, int(nm), int(nn)
    else:
        return False, 0, 0

def generator ():
    for m in range(10, 100):
        for n in range(m + 1, 100):
            result, nm, nn = shares_digit(m, n)
            if result and (m / n == nm / nn):
                yield m, n, nm, nn

def lowest_terms (x, y):
    n = 2
    limit = int(sqrt(max(x, y)) + 0.5)

    for d in range(2, limit + 1):
        if x % n == 0 and y % n == 0:
            return lowest_terms(x // n, y // n)
        n += 1

    return x, y

def main ():
    f = [ (nm, nn) for m, n, nm, nn in generator() ]
    numerator, denominator = reduce(lambda a, p: (a[0] * p[0], a[1] * p[1]), f)

    print(lowest_terms(numerator, denominator))

# :: ---
if __name__ == "__main__":
    main()
