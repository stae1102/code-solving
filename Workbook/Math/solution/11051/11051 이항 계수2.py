import sys
sys.setrecursionlimit(20000)

d = [[0] * (i + 1) for i in range(1001)]

n, k = map(int, input().split())

def solve(n, k):
    if k == 0 or k == n:
        d[n][k] = 1
        return 1
    if d[n][k]:
        return d[n][k]
    else:
        d[n][k] = solve(n - 1, k) + solve(n - 1, k - 1)
        return d[n][k] % 10007

print(solve(n, k) % 10007)