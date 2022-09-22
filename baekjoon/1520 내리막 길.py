import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
d[-1][-1] = 1


def dfs(x, y):
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] > graph[nx][ny]:
                d[x][y] += dfs(nx, ny)

    return d[x][y]


print(dfs(0, 0))
