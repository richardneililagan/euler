#!/usr/bin/env python3

# :: ---

def polygon_generator (c, f):
    n = 1
    p = 0

    while p < 10000:
        p = f(n)
        if p >= 1000:
            s = str(p)
            yield (c, s[:2], s[2:])
        n += 1

def branch_search (candidates, collection):
    if len(candidates) == 6:
        first = candidates[0]
        last = candidates[-1]
        if first[1] == last[2]:
            return candidates
        else:
            return None

    # :: ---
    selected_labels = set(c for (c, s1, s2) in candidates) if len(candidates) != 0 else set()
    last = candidates[-1] if len(candidates) != 0 else (None, None, None)

    pool = set(
        (l, s1, s2)
        for (l, s1, s2) in collection
        if l not in selected_labels
        and s1 == last[2]
    ) if len(candidates) != 0 else collection

    for c in pool:
        result = branch_search(candidates + [c], collection)
        if result != None:
            return result

    return None

def main ():
    triangles = set(x for x in polygon_generator(3, lambda n: (n * (n + 1)) // 2))
    squares = set(x for x in polygon_generator(4, lambda n: n ** 2))
    pentagons = set(x for x in polygon_generator(5, lambda n: (n * (3 * n - 1)) // 2))
    hexagons = set(x for x in polygon_generator(6, lambda n: n * (2 * n - 1)))
    heptagons = set(x for x in polygon_generator(7, lambda n: (n * (5 * n - 3)) // 2))
    octagons = set(x for x in polygon_generator(8, lambda n: n * (3 * n - 2)))

    collection = triangles | squares | pentagons | hexagons | heptagons | octagons

    result = branch_search(list(), collection)
    nums = list(int(s1 + s2) for (_, s1, s2) in result)

    print(sum(nums))

# :: ---
if __name__ == "__main__":
    main()
