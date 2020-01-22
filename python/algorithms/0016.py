#!/usr/bin/env python3

# :: ---

def main ():
    big_number = 2 ** 1000
    digits = map(lambda c: int(c), str(big_number))
    print(sum(digits))

# :: ---
if __name__ == "__main__":
    main()
