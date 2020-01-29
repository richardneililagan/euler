#!/usr/bin/env python3

# :: ---

COINS = [200, 100, 50, 20, 10, 5, 2, 1]
PAIRS = [ (COINS[i], COINS[i + 1]) for i in range(0, len(COINS) - 1) ]

def coin_count (change, i):
    coin = COINS[i]

    # :: short circuit
    if coin == 1:
        return 1

    permutations = change // coin
    sums = [
        coin_count(change - coin * x, i + 1)
        for x in range(0, permutations + 1) 
    ]

    return sum(sums)

def main ():
    print(coin_count(200, 0))

# :: ---
if __name__ == "__main__":
    main()
