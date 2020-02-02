#!/usr/bin/env python3

from itertools import permutations

# :: ---

def generator ():
    digits = set(range(0, 10))
    for p in permutations(digits):
        # :: quick sieve: make sure d4 is divisible by 2
        #    or d6 is divisible by 5
        if (p[3] % 2 == 0) and (p[5] % 5) == 0 and p[0] != 0:
            yield int("".join(map(lambda d: str(d), p)))

def is_divisible (n):
    s = str(n)
    d = [2, 3, 5, 7, 11, 13, 17]

    for i in range(0, len(d)):
        x = int(s[(i + 1):(i + 4)])
        if (x % d[i] != 0):
            return False

    return True

def main ():
    pandigitals = [ x for x in generator() if is_divisible(x) ]
    print(sum(pandigitals))

# :: ---
if __name__ == "__main__":
    main()
