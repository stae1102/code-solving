from collections import deque
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())


def bfs():
    dx, dy, dz = [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 1]
    t = [[] for _ in range(h)]
    starts = []
    days = 0

    for z in range(h):
        for y in range(m):
            tmp = list(map(int, input().split()))
            t[z].append(tmp)
            for x in range(n):
                if tmp[x] == 0:
                    days += 1
                elif tmp[x] == 1:
                    starts.append((z, y, x, 0))

    if days == 0:
        return 0

    q = deque(starts)
    while q:
        z, y, x, d = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n:
                if t[nz][ny][nx] == 0:
                    t[nz][ny][nx] = 1
                    days -= 1
                    if days == 0:
                        return d + 1
                    q.append((nz, ny, nx, d + 1))

    return -1


print(bfs())
