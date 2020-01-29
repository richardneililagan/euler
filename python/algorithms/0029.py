#!/usr/bin/env python3

# :: ---

def generator ():
    ra = range(2, 101)   # :: 2 <= a <= 100
    rb = range(2, 101)   # :: 2 <= b <= 100

    for a in ra:
        for b in rb:
            yield a ** b

def main ():
    s = set([x for x in generator()])
    print(len(s))

# :: ---
if __name__ == "__main__":
    main()
