from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    q = deque([(0, 0, 0, 1)])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    while q:
        x, y, cnt, d = q.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][cnt]:
                if field[nx][ny] == 0 or (field[nx][ny] == 1 and cnt == 0):
                    visited[nx][ny][cnt] = True
                    q.append((nx, ny, cnt + field[nx][ny], d + 1))

    return -1


n, m = map(int, input().split())

field = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())
