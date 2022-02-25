"""
1 -> v1 -> v2 -> n
1 -> v2 -> v1 -> n
"""
import heapq
import sys
import math
input = sys.stdin.readline
n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [math.inf] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
ans = min(case1, case2)
if ans != math.inf:
    print(ans)
else:
    print(-1)
