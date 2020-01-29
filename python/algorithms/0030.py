#!/usr/bin/env python3

from functools import reduce

# :: ---

def length_limit (power):
    """Determine the most number of digits satisfying the algo with specified power."""
    digits = 1
    theoretical_max = lambda d: d * (9 ** power)

    while theoretical_max(digits) >= (10 ** digits):
        digits += 1

    return digits

def is_power_sum (n, power):
    """Determine if n is a sum of its digits raised to the specified power."""
    digits = [ int(d) for d in str(n) ]
    power_sum = reduce(lambda a, d: a + (d ** power), digits, 0)

    return n == power_sum

def main ():
    power = 5
    limit = 10 ** length_limit(power)
    power_sums = [x for x in range(10, limit) if is_power_sum(x, power)]

    print(sum(power_sums))

# :: ---
if __name__ == "__main__":
    main()
