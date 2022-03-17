import heapq
import sys
import math
input = sys.stdin.readline
INF = math.inf

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, end):
    d = [INF] * (n + 1)
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return d[end]

max_time = -1

for i in range(1, n + 1):
    max_time = max(max_time, dijkstra(i, x) + dijkstra(x, i))

print(max_time)