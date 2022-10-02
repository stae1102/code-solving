from collections import deque
import sys
input = sys.stdin.readline

T = int(input())


def topology_sort(graph, indegree, w):
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            cost[i] = max(cost[i], time[i] + cost[now])
            if indegree[i] == 0:
                q.append(i)

    print(cost[w])


for _ in range(T):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    cost, time = [0], [0]

    _ = list(map(int, input().split()))
    cost += _
    time += _

    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())
    topology_sort(graph, indegree, w)
