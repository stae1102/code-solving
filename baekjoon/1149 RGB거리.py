import sys
input = sys.stdin.readline

n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = rgbs[0]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1:]) + rgbs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgbs[i][1]
    dp[i][2] = min(dp[i - 1][:-1]) + rgbs[i][2]

print(min(dp[n - 1]))
