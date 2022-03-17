import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

vips = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1

if m > 0:
    temp = 0
    for i in range(m):
        ans *= dp[vips[i] - temp - 1]
        temp = vips[i]
    ans *= dp[n - temp]
else:
    ans = dp[n]
print(ans)