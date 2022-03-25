n, k = map(int, input().split())

cb = [[1] * (i + 1) for i in range(n + 1)]

cb[1] = [1, 1]

for i in range(2, n + 1):
    for j in range(1, i):
        cb[i][j] = (cb[i - 1][j - 1] + cb[i - 1][j]) % 1000000007

print(cb[n][k])