import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)

for _ in range(m):
    a, b, c  = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    dis[start] = 0
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

start, end = map(int, input().split())
dijkstra(start)
print(dis[end])
