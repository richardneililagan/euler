#!/usr/bin/env python3

# :: ---

def base_generator ():
    n = 0
    yield 9
    while True:
        yield (9 * (10 ** len(str(n))) + n)
        n += 1

def concat (l):
    return "".join(map(lambda n: str(n), l))

def is_pandigital (n):
    b = set(range(1, 10))
    c = set(map(lambda s: int(s), str(n)))

    return n < 1000000000 and len(b ^ c) == 0

def cproduct_generator ():
    max_n = 8
    g = base_generator()

    while max_n > 2:
        max_n = 8
        c_base = next(g)

        aggregate = concat([ c_base * x for x in range(1, max_n) ])
        while len(aggregate) > 9:
            max_n -= 1
            aggregate = concat([ c_base * x for x in range(1, max_n) ])

        yield aggregate

def main ():
    g = cproduct_generator()
    p = [ x for x in g if is_pandigital(int(x)) ]
    print(max(p))

# :: ---
if __name__ == "__main__":
    main()
