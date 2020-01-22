#!/usr/bin/env python3

from functools import reduce
from os.path import dirname, join

# :: ---

letters = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_inputs ():
    filepath = join(dirname(__file__), '../assets/p022_names.txt')
    with open(filepath) as f:
        return sorted(reduce(
            lambda a, v: a + list(map(lambda n: n.replace('"', ''), v.split(','))),
            [ line.strip() for line in f ],
            []
        ))

def get_score (name):
    score = [ letters.index(c) for c in name ]
    return sum(score)

def main ():
    names = get_inputs()
    scores = [ get_score(names[i]) * (i + 1) for i in range(0, len(names)) ]

    print(sum(scores))

# :: ---
if __name__ == "__main__":
    main()
