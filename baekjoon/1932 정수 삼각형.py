import sys
input = sys.stdin.readline

n = int(input())

t = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * i for i in range(1, n + 1)]
d[0] = t[0]

for i in range(n - 1):
    for j in range(len(t[i])):
        d[i + 1][j] = max(d[i + 1][j], d[i][j] + t[i + 1][j])
        d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + t[i + 1][j + 1])

print(max(d[n - 1]))
