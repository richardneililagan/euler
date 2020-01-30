#!/usr/bin/env python3

# :: ---

def shares_digit (m, n):
    sm = list(str(m))
    sn = list(str(n))
    sd = set(sm) & set(sn)

    if len(sd) == 1 and "0" not in sd:
        d = list(sd)[0]
        nm = "".join([ x for x in sm if int(x) != int(d) ])
        nn = "".join([ x for x in sn if int(x) != int(d) ])

        if len(nm) == 0 or len(nn) == 0 or nm >= nn:
            return False, 0, 0
        else:
            return True, int(nm), int(nn)
    else:
        return False, 0, 0

def generator ():
    for m in range(10, 100):
        for n in range(m + 1, 100):
            result, nm, nn = shares_digit(m, n)
            if result and (m / n == nm / nn):
                yield m, n, nm, nn


def main ():
    f = [ x for x in generator() ]
    print(f)

# :: ---
if __name__ == "__main__":
    main()
