from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
p, q = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x, y):
    q = deque([(x, 0)])
    visited[x] = 1

    while q:
        x, cnt = q.popleft()
        if x == y:
            return cnt
        for i in graph[x]:
            if not visited[i]:
                q.append((i, cnt + 1))
                visited[i] = 1
    return -1

print(bfs(p, q))