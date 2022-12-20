from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
W, H = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(H)]

mirror = []

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            mirror.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 첫 시작 포인트를 통해 방향을 파악

def bfs(x, y):
    visited = [[INF] * W for _ in range(H)]
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*' and visited[nx][ny] >= visited[x][y] + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    nx += dx[i]
                    ny += dy[i]
                else:
                    break

    return visited[mirror[1][0]][mirror[1][1]]

ans = bfs(mirror[0][0], mirror[0][1])

print(ans - 1)