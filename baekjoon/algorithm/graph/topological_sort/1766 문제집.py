import heapq
import sys

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

def topology_sort():
    q = []
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    for i in result:
        print(i, end=' ')

topology_sort()