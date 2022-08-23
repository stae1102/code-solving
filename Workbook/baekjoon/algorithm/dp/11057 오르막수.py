import copy
# n = int(input())
n = int(input())

dp = [[] * 10 for _ in range(n + 1)]
dp[1] = [i for i in range(1, 11)]

for i in range(2, n + 1):
    for j in range(10):
        dp[i].append(sum(dp[i - 1][:j + 1]) % 10007)

print(dp[n][-1])