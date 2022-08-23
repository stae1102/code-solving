import sys
import heapq
import math
input = sys.stdin.readline
INF = math.inf

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, end):
    dis = [INF] * (n + 1)
    q = []
    dis[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis[end]

v1, v2 = map(int, input().split())

ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

ans = min(ans1, ans2)

if ans != INF:
    print(ans)
else:
    print(-1)