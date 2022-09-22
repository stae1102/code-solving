import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and graph[i][j] == 1:
            graph[i][j] += min(graph[i - 1][j], graph[i]
                               [j - 1], graph[i - 1][j - 1])
        ans = max(ans, graph[i][j])

print(ans ** 2)
