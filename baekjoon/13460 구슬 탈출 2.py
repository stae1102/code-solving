from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = [[], [], 0]

graph = [list(input().rstrip()) for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == "R":
            start[0] = [i, j]
        elif graph[i][j] == "B":
            start[1] = [i, j]


def bfs():
    visited = [
        [[[False] * 11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    q = deque()
    q.append(start)
    ans = -1
    visited[start[0][0]][start[0][1]][start[1][0]][start[1][1]] = True

    while q:
        r, b, cnt = q.popleft()
        if cnt > 10:
            break
        if graph[r[0]][r[1]] == 'O' and graph[b[0]][b[1]] != 'O':
            ans = cnt
            break

        for i in range(4):
            n_rx, n_ry = r
            n_bx, n_by = b

            while True:
                if graph[n_rx][n_ry] != '#' and graph[n_rx][n_ry] != 'O':
                    n_rx += dx[i]
                    n_ry += dy[i]
                else:
                    if graph[n_rx][n_ry] == '#':
                        n_rx -= dx[i]
                        n_ry -= dy[i]
                    break

            while True:
                if graph[n_bx][n_by] != '#' and graph[n_bx][n_by] != 'O':
                    n_bx += dx[i]
                    n_by += dy[i]
                else:
                    if graph[n_bx][n_by] == '#':
                        n_bx -= dx[i]
                        n_by -= dy[i]
                    break

            if n_rx == n_bx and n_ry == n_by:
                if graph[n_rx][n_ry] != 'O':
                    red = abs(n_rx - r[0]) + abs(n_ry - r[1])
                    blue = abs(n_bx - b[0]) + abs(n_by - b[1])
                    if (red > blue):
                        n_rx -= dx[i]
                        n_ry -= dy[i]
                    else:
                        n_bx -= dx[i]
                        n_by -= dy[i]
            if visited[n_rx][n_ry][n_bx][n_by] == False:
                visited[n_rx][n_ry][n_bx][n_by] = True
                q.append([(n_rx, n_ry), (n_bx, n_by), cnt + 1])

    return ans


print(bfs())
