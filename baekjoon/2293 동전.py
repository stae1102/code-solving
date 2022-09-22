import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readlines()))

d = [0] * (k + 1)
d[0] = 1


def plus_coin(idx, coin):
    while idx <= k:
        d[idx] += d[idx-coin]
        idx += 1
    return


for coin in coins:
    plus_coin(coin, coin)

print(d[k])
