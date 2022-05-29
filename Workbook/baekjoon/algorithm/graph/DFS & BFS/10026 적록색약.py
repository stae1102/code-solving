from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 색약이 없는 사람일 때
def bfs(x, y):
    q = deque([(x, y, graph[x][y])])
    visited[x][y] = 1

    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == c:
                if visited[nx][ny] == 0:
                    q.append((nx, ny, graph[nx][ny]))
                    visited[nx][ny] = 1

def bfs2(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'B':
                if visited[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 0

RGB = {'R':0, 'G':0, 'B':0}
RG = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            RGB[graph[i][j]] += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 'B' and visited[i][j] == 1:
            RG += 1
            bfs2(i, j)

print(RGB['R'] + RGB['G'] + RGB['B'], RG + RGB['B'])