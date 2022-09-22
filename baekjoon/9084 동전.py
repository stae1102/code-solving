import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())

    d = [0] * (k + 1)
    d[0] = 1
    for coin in coins:
        for j in range(coin, k + 1):
            d[j] += d[j - coin]

    print(d[k])
