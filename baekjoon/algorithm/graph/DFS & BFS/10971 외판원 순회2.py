import sys
input = sys.stdin.readline

n = int(input())
graph = [[] * n for _ in range(n)]
visited = [False] * n
dist = int(1e9)

for i in range(n):
    graph[i] = list(map(int, input().split()))

def dfs(start, prev, i, cost):
    global dist

    if i == n - 1:
        if graph[prev][start] != 0:
            cost += graph[prev][start]
            dist = min(dist, cost)
        return 
    
    for j in range(n):
        if not visited[j] and graph[prev][j] != 0 and cost < dist:
            visited[j] = True
            dfs(start, j, i + 1, cost + graph[prev][j])
            visited[j] = False
    
for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, i, 0, 0)

print(dist)