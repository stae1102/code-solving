import sys
input = sys.stdin.readline

dx = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 1, 2], [0, 1, 1, 2], [0, 0, 0, 1], [0, 0, 0, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 0, 0, -1], [0, 1, 1, 1], [0, 1, 2, 0], [0, 0, 1, 2], [0, 1, 1, 1], [-1, -1, -1, 0], [-1, 0, 1, 0], [0, -1, 0, 1]]

dy = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 1, 0, 1], [0, 1, 1, 2], [-2, -1, -1, 0], [0, 0, -1, -1], [0, 0, 1, 1], [0, 1, 2, 2],[0, 1, 2, 0], [0, 0, 0, -1], [0, 0, 0, 1], [0, 1, 2, 2], [0, 0, 1, 2], [0, 0, 0, 1], [0, 1, 1, 1], [0, -1, 0, 1], [-1, 0, 1, 0], [-1, -1, -1, 0], [0, 1, 1, 1]]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = -1

for x in range(n):
    for y in range(m):
        for i, j in zip(dx, dy):
            cnt = 0
            a1, a2, a3, a4 = map(lambda k: k + x, i)
            b1, b2, b3, b4 = map(lambda k: k + y, j)
            if (0 <= a1 < n and 0 <= a2 < n and 0 <= a3 < n and 0 <= a4 < n) and (0 <= b1 < m and 0 <= b2 < m and 0 <= b3 < m and 0 <= b4 < m):
                cnt += graph[a1][b1] + graph[a2][b2] + graph[a3][b3] + graph[a4][b4]
                ans = max(ans, cnt)

print(ans)