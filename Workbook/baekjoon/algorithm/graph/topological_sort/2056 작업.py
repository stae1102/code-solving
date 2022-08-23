import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
cost = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]
    if temp[1] == 0:
        continue
    for j in temp[2:]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    q = deque()
    result = cost[:]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + cost[i])
            if indegree[i] == 0:
                q.append(i)

    print(max(result))

topology_sort()