#!/usr/bin/env python3

from collections import Counter
from os.path import dirname, join
from functools import reduce

# :: ---

CARD_VALUES = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

SCORE_BASE = 10

def card_value (c):
    v = CARD_VALUES.get(c[0], c[0])
    return int(v), c[1]

def hand_value (h):
    return 10**10 * 9 + int("".join(map(lambda v: '%02d' % v, h)))

def hands_generator ():
    lines = get_inputs()

    for line in lines:
        cards = list(map(card_value, line.split(' ')))

        p1 = cards[:5]
        p2 = cards[5:]

        yield p1, p2

def is_royalflush (h):
    faces = map(lambda c: c[0], h)
    if is_flush(h) and min(faces) == 10:
        return SCORE_BASE**12
    return 0

def is_straightflush (h):
    is_f = is_flush(h)
    is_s = is_straight(h)
    if is_f and is_s:
        s = sorted(map(lambda c: c[0], h), reverse = True)
        return (SCORE_BASE**11) * 8 + (is_s - 10**11 * 4)
    return 0

def is_fourofakind (h):
    faces = Counter(map(lambda c: c[0], h))
    g = faces.most_common()
    if g[0][1] == 4:
        h = [g[0][0]] * 4 + [g[1][0]]
        return (SCORE_BASE**11) * 7 + hand_value(h)
    return 0

def is_fullhouse (h):
    faces = Counter(map(lambda c: c[0], h))
    g = faces.most_common(2)
    if g[0][1] == 3 and g[1][1] == 2:
        h = [g[0][0]] * 3 + [g[1][0]] * 2
        return (SCORE_BASE**11) * 6 + hand_value(h)
    return 0

def is_flush (h):
    suits = set(map(lambda c: c[1], h))
    if len(suits) == 1:
        s = sorted(map(lambda c: c[0], h), reverse = True)
        return (SCORE_BASE**11) * 5 + hand_value(s)
    return 0

def is_straight (h):
    faces = sorted(map(lambda c: c[0], h), reverse = True)
    # :: account for ace-low straights
    lfaces = sorted((1 if x == 14 else x for x in faces), reverse = True)
    if (max(faces) - min(faces)) == 4:
        return (SCORE_BASE**11) * 4 + hand_value(faces)
    elif (max(lfaces) - min(lfaces)) == 4:
        return (SCORE_BASE**11) * 4 + hand_value(lfaces)
    return 0

def is_threeofakind (h):
    faces = Counter(map(lambda c: c[0], h))
    g = faces.most_common()
    if g[0][1] == 3:
        s = sorted(map(lambda c: c[0], h), reverse = True)
        return (SCORE_BASE**11) * 3 + hand_value(s)
    return 0

def is_twopair (h):
    faces = Counter(map(lambda c: c[0], h))
    g = faces.most_common()
    if g[0][1] == 2 and g[1][1] == 2:
        s = sorted(map(lambda c: c[0], h), reverse = True)
        return (SCORE_BASE**11) * 2 + hand_value(s)
    return 0

def is_onepair (h):
    s = sorted(map(lambda c: c[0], h), reverse = True)
    faces = Counter(map(lambda c: c[0], h))
    g = faces.most_common()
    if len(faces) == 4:
        return SCORE_BASE**11 + hand_value(s)
    return 0

def is_highcard (h):
    s = sorted(map(lambda c: c[0], h), reverse = True)
    return hand_value(s)

def score_hand (h):
    scorers = [
        is_royalflush,
        is_straightflush,
        is_fourofakind,
        is_fullhouse,
        is_flush,
        is_straight,
        is_threeofakind,
        is_twopair,
        is_onepair,
        is_highcard
    ]

    score = reduce(lambda a, f: a or f(h), scorers, 0)
    return score

def get_inputs():
    filepath = join(dirname(__file__), '../assets/p054_poker.txt')
    with open(filepath) as f:
        return [ line.strip() for line in f ]

def main ():
    g = hands_generator()
    h = [(14, 'S'), (14, 'S'), (3, 'S'), (3, 'S'), (3, 'S')]
    print("royalflush:", is_royalflush(h))
    print("straightflush:", is_straightflush(h))
    print("fourofakind:", is_fourofakind(h))
    print("fullhouse:", is_fullhouse(h))
    print("flush:", is_flush(h))
    print("straight:", is_straight(h))
    print("threeofakind:", is_threeofakind(h))
    print("twopair:", is_twopair(h))
    print("onepair:", is_onepair(h))
    print("highcard:", is_highcard(h))
    print(score_hand(h))

    print(len(
        [ 1 for x, y in g if score_hand(x) > score_hand(y) ]
    ))

# :: ---
if __name__ == "__main__":
    main()
