from collections import deque
import sys
input = sys.stdin.readline


def bfs(cost):
    q = deque([start])
    visited[start] = True

    while q:
        x = q.popleft()
        if x == end:
            return True
        for i in graph[x]:
            if not visited[i[0]] and cost <= i[1]:
                visited[i[0]] = True
                q.append(i[0])

    return False


# deque를 통한 너비 우선 탐색
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

max_cost = -1

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    max_cost = max(max_cost, cost)

start, end = map(int, input().split())

pl, pr = 1, max_cost

while pl <= pr:
    mid = (pl + pr) // 2
    visited = [False] * (n + 1)

    if bfs(mid):
        pl = mid + 1
    else:
        pr = mid - 1

print(pr)
