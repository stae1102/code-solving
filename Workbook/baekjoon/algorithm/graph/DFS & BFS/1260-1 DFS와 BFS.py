from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, N + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = False
    q = deque([v])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)