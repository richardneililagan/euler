#!/usr/bin/env python3

# :: ---

def generator (xMax, yMax):
    x = 100

    while x < xMax:
        y = 100

        while y < yMax:
            yield x * y
            y += 1
        x += 1

def isPalindromic (num):
    return str(num) == str(num)[::-1]

def main ():
    numbers = [ x for x in generator(1000, 1000) if isPalindromic(x) ]
    numbers.sort(reverse = True)

    print(numbers[0])

# :: ---
if __name__ == "__main__":
    main()
