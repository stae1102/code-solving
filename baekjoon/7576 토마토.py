from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int, input().split())

t = []
starts = []
remain = 0

for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 0:
            remain += 1
        elif tmp[j] == 1:
            starts.append((i, j, 0))
    t.append(tmp)


def bfs():
    global remain
    q = deque(starts)

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and t[nx][ny] == 0:
                t[nx][ny] = 1
                remain -= 1
                if remain == 0:
                    return d + 1
                q.append((nx, ny, d + 1))

    return -1


if remain != 0:
    print(bfs())
else:
    print(0)
