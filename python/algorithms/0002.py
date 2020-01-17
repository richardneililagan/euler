#!/usr/bin/env python3

# :: ---

def fibonacci (maxNum):
    num1 = 0
    num2 = 1

    while (num1 + num2) < maxNum:
        sink = num1 + num2
        num1 = num2
        num2 = sink
        yield num2

def main ():
    def filter (x): return (x % 2 == 0)

    total = sum([x for x in fibonacci(4000000) if filter(x)])
    print(total)

# :: ---
if __name__ == "__main__":
    main()
