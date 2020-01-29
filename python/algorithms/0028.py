#!/usr/bin/env python3

from itertools import islice

# :: ---

def generator (step = 2):
    n = 3
    while True:
        yield n, (n - step)
        n += step

def square_generator ():
    g = generator()
    while True:
        a, b = next(g)
        step = ((a ** 2) - (b ** 2)) / 4
        corners = map(lambda x: (b ** 2) + (step * x), range(1, 5))
        yield int(sum(corners))

def main ():
    sg = square_generator()
    l = islice(sg, 500)

    print(sum(l) + 1)

# :: ---
if __name__ == "__main__":
    main()
