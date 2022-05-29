import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 2)]
for i in range(1, n + 1):
    t, p = map(int, sys.stdin.readline().split())
    dp[i] = max(dp[i - 1], dp[i])
    if i + t > n + 1: continue
    dp[i + t] = max(dp[i] + p, dp[i + t])
dp[n + 1] = max(dp[n + 1], dp[n])
print(dp[n + 1])