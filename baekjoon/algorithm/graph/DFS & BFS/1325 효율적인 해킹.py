from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, v):
    queue = deque([v])
    visited = [False] * (n + 1)
    cnt = 1
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = {}

for i in range(1, n + 1):
    if graph[b]:
        ans[i] = bfs(graph, i)

max_num = max(ans.values())

print(*sorted([i for (i, j) in ans.items() if j == max_num]))
