#!/usr/bin/env python3

from functools import lru_cache, reduce
from os.path import dirname, join

# :: ---

letters = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

@lru_cache(maxsize = None)
def tn (n):
    return 0.5 * n * (n + 1)

@lru_cache(maxsize = None)
def is_tn (n):
    c = 0
    i = 0

    while c < n:
        i += 1
        c = tn(i)

    return c == n

def get_score (word):
    s = map(lambda c: letters.index(c), word)
    return sum(s)

def get_inputs ():
    filepath = join(dirname(__file__), '../assets/p042_words.txt')
    with open(filepath) as f:
        return reduce(
            lambda a, v: a + list(
                map(lambda n: n.replace('"', ''), v.split(','))
            ),
            [ line.strip() for line in f ],
            []
        )

def main ():
    w = [ x for x in get_inputs() if is_tn(get_score(x)) ]
    print(len(w))

# :: ---

if __name__ == "__main__":
    main()
