from sys import stdin
from collections import deque

read = stdin.readline
N, M, V = map(int, read().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):    # 양방향 연결을 통한 그래프 전개
    x, y = map(int, read().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):    # 재귀를 통해 dfs 구현
    visited[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)

def bfs(V):    # 데크를 통해 bfs 
    visited[V] = False
    queue = deque([V])
    while queue:
        V = queue.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()
bfs(V)
