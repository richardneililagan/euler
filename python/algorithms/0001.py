#!/usr/bin/env python3

from functools import reduce

# :: ---

def main ():
    def filter (x): return (x % 3 == 0) or (x % 5 == 0)
    def reducer (a, v): return a + v

    numbers = range(1, 1000)    # :: 1 - 999
    multiples = [ x for x in numbers if filter(x) ]
    total = reduce(reducer, multiples)

    print(total)

# :: ---
if __name__ == "__main__":
    main()
