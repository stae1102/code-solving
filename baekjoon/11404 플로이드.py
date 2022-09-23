import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

distances = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distances[i][i] = 0

for _ in range(m):
    i, j, w = map(int, input().split())
    distances[i][j] = min(distances[i][j], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distances[i][j] = min(
                distances[i][j], distances[i][k] + distances[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distances[i][j] == INF:
            print(0, end=" ")
        else:
            print(distances[i][j], end=" ")
    print()
