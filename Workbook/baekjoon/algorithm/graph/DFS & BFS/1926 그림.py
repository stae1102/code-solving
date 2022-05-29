from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == 0:
        return 0
    q = deque([(x, y)])
    graph[x][y] = 0
    area = 0
    while q:
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    return area

cnt = 0
areas = []

for a in range(n):
    for b in range(m):
        temp = bfs(a, b)
        if temp > 0:
            cnt += 1
            areas.append(temp)

print(cnt)
if areas:
    print(max(areas))
else:
    print(0)