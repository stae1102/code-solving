<<<<<<< HEAD
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited_lab = [[0] * m for _ in range(n)]
visited_wall = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
def bfs():
    global ans

    q = deque()

    # 바이러스 위치 파악하여 퍼질 수 있는 곳 체크
    for x in range(n):
        for y in range(m):
            # visited_lab[x][y]가 0이기만 하면 방문하지 않은 것이니까 그냥 값을 저장
            visited_lab[x][y] = graph[x][y]
            if graph[x][y] == 2:
                q.append((x, y))
                visited_lab[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 방문한 좌표가 이미 방문했거나 바이러스거나 벽이 아니라면
            if 0 <= nx < n and 0 <= ny < m and not visited_lab[nx][ny]:
                visited_lab[nx][ny] = 1
                q.append((nx, ny))

    temp = 0
    for x in range(n):
        for y in range(m):
            if not visited_lab[x][y]:
                temp += 1

    ans = max(ans, temp)

def bt(depth, _x):
    if depth == 3:
        bfs()
        return

    for x in range(_x, n):
        for y in range(m):
            if not graph[x][y] and not visited_wall[x][y]:
                visited_wall[x][y] = 1
                graph[x][y] = 1
                bt(depth + 1, x)
                visited_wall[x][y] = 0
                graph[x][y] = 0

bt(0, 0)
=======
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited_lab = [[0] * m for _ in range(n)]
visited_wall = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
def bfs():
    global ans

    q = deque()

    # 바이러스 위치 파악하여 퍼질 수 있는 곳 체크
    for x in range(n):
        for y in range(m):
            # visited_lab[x][y]가 0이기만 하면 방문하지 않은 것이니까 그냥 값을 저장
            visited_lab[x][y] = graph[x][y]
            if graph[x][y] == 2:
                q.append((x, y))
                visited_lab[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            # 방문한 좌표가 이미 방문했거나 바이러스거나 벽이 아니라면
            if 0 <= nx < n and 0 <= ny < m and not visited_lab[nx][ny]:
                visited_lab[nx][ny] = 1
                q.append((nx, ny))

    temp = 0
    for x in range(n):
        for y in range(m):
            if not visited_lab[x][y]:
                temp += 1

    ans = max(ans, temp)

def bt(depth, _x):
    if depth == 3:
        bfs()
        return

    for x in range(_x, n):
        for y in range(m):
            if not graph[x][y] and not visited_wall[x][y]:
                visited_wall[x][y] = 1
                graph[x][y] = 1
                bt(depth + 1, x)
                visited_wall[x][y] = 0
                graph[x][y] = 0

bt(0, 0)
>>>>>>> origin/ubuntu
print(ans)