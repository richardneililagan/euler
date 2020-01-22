#!/usr/bin/env python3

from functools import lru_cache
from operator import itemgetter

# :: ---

@lru_cache(maxsize = None)
def collatz_length (n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_length(n / 2)
    else:
        return 1 + collatz_length((3 * n) + 1)

def main ():
    lengths = [ (n, collatz_length(n)) for n in range(1, 1000000) ]
    print(max(lengths, key = itemgetter(1)))

# :: ---
if __name__ == "__main__":
    main()
