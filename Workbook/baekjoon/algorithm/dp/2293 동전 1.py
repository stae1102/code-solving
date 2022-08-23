import sys
sys.setrecursionlimit = int(1e9)
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

def plus_coin(idx, coin):
    while idx <= k:
        dp[idx] += dp[idx-coin]
        idx += 1
    return

for coin in coins:
    plus_coin(coin, coin)

print(dp[k])