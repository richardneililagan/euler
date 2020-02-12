#!/usr/bin/env python3

from collections import Counter

# :: ---

def generator (starting_power = 3):
    n = starting_power

    while True:
        for x in range(10 ** n, (10 ** (n + 1)) // 6):
            yield list(map(lambda a: x * a, range(1, 7)))
        n += 1

def is_valid (s):
    digits = list(map(lambda v: list(str(v)), s))
    a = Counter(digits[0])
    b = map(lambda v: Counter(v) == a, digits[1:])
    return all(b)

def main ():
    g = generator()
    while True:
        s = next(g)
        if is_valid(s):
            print(s[0])
            return

# :: ---
if __name__ == "__main__":
    main()
