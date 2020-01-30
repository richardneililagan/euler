#!/usr/bin/env python3

from itertools import permutations

# :: ---

# :: We're assuming that if we're interested in using the digits 1 - 9 once each,
#    then our multiplicant and multiplier can only be of the following lengths:
#
#    - (1d x 4d) or (4d x 1d)
#    - (2d x 3d) or (3d x 2d)

digits = set(list("123456789"))

def p_concat (p):
    return int("".join(map(lambda d: str(d), p)))

def generator ():
    # :: (a x b = c)
    for da in [1, 2]:
        for pa in permutations(digits, da):
            sb = digits.copy() ^ set(pa)
            for pb in permutations(sb, 5 - da):
                a = p_concat(pa)
                b = p_concat(pb)
                product = a * b
                sc = sb.copy() ^ set(pb) ^ set(list(str(product)))

                if len(sc) == 0 and len(str(product)) == len(set(list(str(product)))):
                    yield product

def main ():
    pandigitals = [ x for x in generator() ]
    print(sum(set(pandigitals)))

# :: ---
if __name__ == "__main__":
    main()
