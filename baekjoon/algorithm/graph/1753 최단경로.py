import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c  = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    dis[start] = 0
    visited[start] = True
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dis[now] + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
