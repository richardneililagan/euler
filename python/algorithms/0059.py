#!/usr/bin/env python3

from os.path import dirname, join
from itertools import combinations_with_replacement

# :: ---

common_words = [ (' ' + x + ' ') for x in 'the|be|to|of|and|a|in|that|have|it|for|not|on|with|he|as|you|do|at|this|but|his|by|from|they|we'.split('|') ]

def get_input ():
    filepath = join(dirname(__file__), '../assets/p059_cipher.txt')
    with open(filepath) as f:
        l = [ line.strip() for line in f ]
        return list(map(lambda c: int(c), l[0].split(',')))

def key_generator ():
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                yield (a, b, c)

def decrypt (cipher, key):
    return [ x ^ key[i % len(key)] for i, x in enumerate(cipher) ]

def to_text (codes):
    return "".join([ chr(x) for x in codes ]).lower()

def english_score (t):
    matches = sum(1 for word in common_words if word in t)
    return matches / len(common_words)

def main ():
    cipher = get_input()
    keys = key_generator()
    originals = (decrypt(cipher, k) for k in keys)

    candidate = max(
        ((english_score(to_text(o)), o) for o in originals),
        key = lambda item: item[0]
    )

    print(sum(candidate[1]))

# :: ---
if __name__ == "__main__":
    main()
