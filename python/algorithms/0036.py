#!/usr/bin/env python3

# :: ---

MAX_LIMIT = 1000000

def is_palindromic (s):
    rs = "".join(s[::-1])
    return s == rs

def to_b (n):
    return "{0:b}".format(n)

def main ():
    b10_palindromes = [
        x for x
        in range(1, MAX_LIMIT)
        if is_palindromic(str(x))
        and is_palindromic(to_b(x))
    ]

    print(sum(b10_palindromes))

# :: ---
if __name__ == "__main__":
    main()
