import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k + 1)
w = []
v = []

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(n):
    for j in range(k, w[i]-1, -1):
        dp[j] = max(dp[j - w[i]] + v[i], dp[j])

print(dp[k])