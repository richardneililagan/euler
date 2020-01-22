#!/usr/env/bin python3

from functools import reduce

# :: ---

def contract (l):
    return [ (l[x-1] + l[x]) for x in range(1, len(l)) ]

def expand (l):
    return [1] + contract(l) + [1]

def main ():
    middle_row = reduce(
        lambda a, _: expand(a),
        range(20),
        [1]
    )

    projection = reduce(
        lambda a, _: contract(a),
        range(20),
        middle_row
    )

    print(projection[0])

# :: ---
if __name__ == "__main__":
    main()
