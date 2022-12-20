from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]
q = deque()

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

# result = 0

def bfs():
    do = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    do += 1
                elif graph[i][j][k] == 1:
                    q.append((0, i, j, k))

    if do == 0:
        return 0

    while q:
        cnt, z, y, x = q.popleft()

        # if do == 0:
        #     if cnt != 0:
        #         cnt +=1
        #     return cnt

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            # print(nz, ny, x, nx)
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                # print(nz, ny, nx)
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    do -= 1
                    if do == 0:
                        return cnt + 1
                    q.append((cnt + 1, nz, ny, nx))
    
    return -1

print(bfs())