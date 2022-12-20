from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    visited[x][y][0] = 1
    q = deque()
    # q(cnt, x, y, w)
    q.append((1, 0, 0, 0))

    while q:
        cnt, x, y, w = q.popleft()

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][w]:
                if graph[nx][ny] == '1' and w == 0:
                    visited[nx][ny][w] = 1
                    q.append((cnt + 1, nx, ny, w + 1))
                elif graph[nx][ny] == '0':
                    visited[nx][ny][w] = 1
                    q.append((cnt + 1, nx, ny, w))

    return -1


print(bfs(0, 0))
