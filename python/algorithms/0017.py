#!/usr/bin/env python3

# :: ---

digits = [
    "", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
]

def parse_thousands (n):
    i = n // 1000
    words = [
        digits[i],
        "thousand" if i > 0 else ""
    ]

    return "".join(words)

def parse_hundreds (n):
    hundreds = n - ((n // 1000) * 1000)
    i = hundreds // 100

    if i == 0:
        return ""
    else:
        return digits[i] + "hundred"

def parse_tens_and_ones (n):
    one_tens_constructs = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens_constructs = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    tens = n - ((n // 100) * 100)
    i = tens // 10
    j = tens % 10

    words = [
        "and" if n > 100 and n % 100 != 0 else "",
        one_tens_constructs[j] if i == 1 else "",
        tens_constructs[i] if i != 1 else "",
        digits[j] if i != 1 else ""
    ]

    return "".join(words)

def parse_number (n):
    words = [
        parse_thousands(n),
        parse_hundreds(n),
        parse_tens_and_ones(n)
    ]

    return "".join(words)

def main ():
    lengths = [ len(parse_number(x + 1)) for x in range(0, 1000) ]
    print(sum(lengths))

# :: ---
if __name__ == "__main__":
    main()
