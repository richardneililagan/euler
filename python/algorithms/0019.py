#!/usr/bin/env python3

# :: ---

def month_generator (year, month):
    limits = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month != 1:          # :: not February
        max_days = limits[month]
    elif year % 4 != 0:     # :: not a leap year
        max_days = 28
    elif year % 400 == 0:   # :: a leap year for sure
        max_days = 29
    elif year % 100 == 0:   # :: leap year exception
        max_days = 28
    else:                   # :: normal leap year
        max_days = 29

    for date in range(0, max_days):
        yield date

def year_generator (year):
    for m in range(0, 12):
        month = month_generator(year, m)
        for date in month:
            yield date

def century_generator (start_year):
    for y in range(start_year, start_year + 100):
        year = year_generator(y)
        for date in year:
            yield date

def main ():
    g  = century_generator(1901)
    sundays = [ d for d in g ][5::7]    # :: 01/01/1901 was a Tuesday, so Sunday is index 5
    first_day_sundays = [ d for d in sundays if d == 0 ]

    print(len(first_day_sundays))

# :: ---

if __name__ == "__main__":
    main()
