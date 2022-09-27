n, k = map(int, input().split())
d = [[0] * (k + 1) for _ in range(n + 1)]
div = 1000000000

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j == 1:
            d[i][j] = 1
        elif i == 1:
            d[i][j] = j
        else:
            d[i][j] = (d[i - 1][j] + d[i][j - 1]) % div

print(d[n][k])
