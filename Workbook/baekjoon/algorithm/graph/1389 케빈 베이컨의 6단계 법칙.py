import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

connection = [0] * (n + 1)

min_val = INF
min_idx = 0

for i in range(1, n + 1):
    sum_val = sum(graph[i][1:])
    if sum_val < min_val:
        min_val = sum_val
        min_idx = i

print(min_idx)