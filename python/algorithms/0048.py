#!/usr/bin/env python3

# :: ---

def main ():
    s = str(sum([ x ** x for x in range(1, 1001) ]))
    print(s[len(s)-10:])

# :: ---
if __name__ == "__main__":
    main()
