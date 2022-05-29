from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

w, h = map(int, input().split())
graph = [[] for _ in range(h)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)] # 방문 테이블

for i in range(h):
    graph[i] = list(map(int, input().split()))

dist = float('inf')

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

def bfs():
    global dist
    q = deque()
    q.append((0, 0, 0, 0))
    visited[0][0][0] = 1

    # cnt: 총 돌아다닌 횟수, x & y: 좌표, w: 말 걸음 수
    while q:
        cnt, x, y, j = q.popleft()

        # 도착했을 때
        if x == h - 1 and y == w - 1:
            dist = min(dist, cnt)
            return
            # continue

        if j < k:
            # 말 걸음으로 방문 처리
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1:
                    if visited[nx][ny][j + 1] == 0:
                        visited[nx][ny][j + 1] = 1
                        q.append((cnt + 1, nx, ny, j + 1))

        # 원숭이 걸음으로 방문 처리
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1:
                if visited[nx][ny][j] == 0:
                    visited[nx][ny][j] = 1
                    q.append((cnt + 1, nx, ny, j))

bfs()

if dist == float('inf'):
    print(-1)
else:
    print(dist)