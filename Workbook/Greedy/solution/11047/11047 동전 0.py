import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0

for coin in coins[::-1]:
    if coin <= K:
        ans += K // coin
        K %= coin

print(ans)