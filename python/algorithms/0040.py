#!/usr/bin/env python3

from functools import reduce

# :: ---

def champernowne (max_digits = 1000000):
    n = 1
    yielded = 0

    while yielded < max_digits:
        s = str(n)
        for d in s:
            yield int(d)
            yielded += 1
        n += 1

def main ():
    g = champernowne(1000000)

    indices = [ 10 ** x - 1 for x in range(0, 7) ]
    digits = [ x for i, x in enumerate(g) if i in indices ]
    product = reduce(lambda a, v: a * v, digits)

    print(product)

# :: ---
if __name__ == "__main__":
    main()
