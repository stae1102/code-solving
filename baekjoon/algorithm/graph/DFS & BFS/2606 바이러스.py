from sys import stdin
from collections import deque
input = stdin.readline
n, m = int(input()), int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
virus = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    global virus
    visited[v] = True
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)
            virus += 1

def bfs(v):
    global virus
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        virus += 1
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

# dfs(1)
bfs(1)
print(virus - 1)
