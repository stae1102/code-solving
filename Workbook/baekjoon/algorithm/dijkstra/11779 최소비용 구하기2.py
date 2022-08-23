import heapq
import sys
import math
input = sys.stdin.readline
INF = math.inf

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
order = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    order[start] = [start]
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                order[i[0]] = order[now] + [i[0]]
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])
print(len(order[end]))
print(*order[end])