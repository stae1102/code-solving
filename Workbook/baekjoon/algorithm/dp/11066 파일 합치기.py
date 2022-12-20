import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    novel = [0] + list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(k + 1)]

    for i in range(2, k + 1):
        for j in range(1, k + 1 - (i - 1)):
            dp[j][j + i - 1] = min(dp[j][j + n] + dp[j + n + 1][j + i - 1] for n in range(i - 1)) + sum(novel[j:j + i])

    print(dp[1][k])