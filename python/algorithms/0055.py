#!/usr/bin/env python3

# :: ---

def reverse_sum_generator (start):
    reverse_sum = lambda n: n + int(str(n)[::-1])
    a = start

    for _ in range(50):
        a = reverse_sum(a)
        yield a

def lychrel_generator (start, end):
    for n in range(start, end):
        g = reverse_sum_generator(n)
        s = next((1 for x in g if is_palindromic(x)), 0)
        if s == 0:
            yield n

def is_palindromic (n):
    rn = int(str(n)[::-1])
    return n == rn

def main ():
    g = lychrel_generator(1, 10000)
    s = sum(1 for x in g)
    print(s)

# :: ---
if __name__ == "__main__":
    main()
