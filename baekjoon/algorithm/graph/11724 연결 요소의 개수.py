from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
