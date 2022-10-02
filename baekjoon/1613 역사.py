import sys
input = sys.stdin.readline
INF = float('inf')
n, k = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    i, j = map(int, input().split())
    graph[i][j] = -1
    graph[j][i] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] == graph[k][b] != INF:
                graph[a][b] = graph[a][k]

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])
