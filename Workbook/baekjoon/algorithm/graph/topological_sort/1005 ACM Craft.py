from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    time = [0] * (n + 1)
    indegree = [0] * (n + 1)
    result = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    data = list(map(int, input().split()))
    time[1:] = data
    result[1:] = data

    for _ in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        graph[x].append(y)
  
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)
    
    print(result[int(input())])