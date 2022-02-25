from collections import deque
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
m = 100001
visited = [False] * m

def bfs(v):
    q = deque([[v, 0]])
    while q:
        v, x = q.popleft()
        if not visited[v]:
            visited[v] = True
            if v == k:
                return x
            x += 1
            if v - 1 >= 0:
                q.append([v - 1, x])
            if v + 1 <= 100000:
                q.append([v + 1, x])
            if 2 * v <= 100000:
                q.append([2 * v, x])

print(bfs(n))