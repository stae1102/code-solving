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
def start(x, y):
    start_point = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':
            start_point.append((nx, ny))

    return start_point

def bfs(start_point, prev_point):
    # visited = [[INF] * W for _ in range(H)]
    q = deque()
    x, y = start_point
    visited[x][y] = 0
    q.append((x, y, prev_point))

    while q:
        x, y, prev_point = q.popleft()
        direction = [abs(prev_point[0] - x), abs(prev_point[1] - y)]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':
                if direction == [abs(dx[i]), abs(dy[i])]:
                    if visited[nx][ny] <= visited[x][y]:
                        continue
                    visited[nx][ny] = visited[x][y]
                else:
                    if visited[nx][ny] <= visited[x][y]:
                        continue
                    visited[nx][ny] = min(visited[nx][ny], visited[x][y] + 1)
                q.append((nx, ny, (x, y)))
    # return visited

start_point = start(mirror[0][0], mirror[0][1])
visited = [[INF] * W for _ in range(H)]
visited[mirror[0][0]][mirror[0][1]] = 0
for i in start_point:
    bfs(i, mirror[0])
    for i in visited:
        for j in i:
            if j == INF:
                print('*', end='')
                continue
            print(j, end='')
        print()
print(start_point)

print(visited[mirror[1][0]][mirror[1][1]])