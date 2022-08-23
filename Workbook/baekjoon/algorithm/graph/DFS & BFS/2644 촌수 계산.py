from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d1, d2 = map(int, input().split())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    y, x = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start, end):
    queue = deque([(0, start)])
    visited[start] = True
    while queue:
        cost, y = queue.popleft()
        if y == end:
            return cost
        for x in graph[y]:
            if not visited[x]:
                queue.append((cost + 1, x))
                visited[x] = True
    return -1

print(bfs(graph, d1, d2))