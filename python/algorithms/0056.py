#!/usr/bin/env python3

# :: ---

def digital_sum (n):
    return sum(map(lambda d: int(d), str(n)))

def generator ():
    for a in range(100):
        for b in range(100):
            yield digital_sum(a ** b)

def main ():
    g = generator()
    print(max(x for x in g))

# :: ---
if __name__ == "__main__":
    main()
