#!/usr/bin/env python3

from functools import lru_cache, reduce

# :: ---

# :: since 9! == 362880, we can potentially get a 7-digit candidate
#    because 9999999 will yield an algorithmic sum of 2540160 (not a correct candidate).
#  
# :: TODO find a better upper bounds calculation.

@lru_cache(maxsize = None)
def factorial (n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fsum (n):
    return reduce(
        lambda a, v: a + v,
        map(lambda d: factorial(int(d)), str(n))
    )

def main ():
    candidates = [ x for x in range(10, 2540160) if x == fsum(x) ]
    print(sum(candidates))

# :: ---
if __name__ == "__main__":
    main()
