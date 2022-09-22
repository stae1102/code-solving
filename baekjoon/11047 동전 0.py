import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = list(map(int, sys.stdin.readlines()))

cnt = 0
for coin in coins[::-1]:
    if coin <= k:
        cnt += k // coin
        k %= coin
        if k == 0:
            print(cnt)
            break
