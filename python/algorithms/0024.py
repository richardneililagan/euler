#!/usr/bin/env python3

from itertools import islice
from functools import reduce

# :: ---

def generator (s):
    if len(s) == 1:
        yield [next(iter(s))]
        return

    # :: ---
    for d in s:
        subset = s.copy()
        subset.remove(d)
        g = generator(subset)

        for t in g:
            yield [d] + t

def main ():
    g = generator(set([0,1,2,3,4,5,6,7,8,9]))

    l = list(islice(g, 1000000))
    num = reduce(lambda a, v: a + str(v), l[999999], "")

    print(num)

# :: ---
if __name__ == "__main__":
    main()
