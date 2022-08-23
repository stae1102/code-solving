import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
W, H = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(H)]
visited = [[INF] * W for _ in range(H)]

mirror_cnt = 0
mx1, my1, mx2, my2 = 0, 0, 0, 0

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            if mirror_cnt == 0:
                mx1, my1 = i, j
                mirror_cnt += 1
            else:
                mx2, my2 = i, j
                break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
ans = INF
# (cnt, direction, x, y)
heapq.heappush(q, (0, 0, mx1, my1))
heapq.heappush(q, (0, 1, mx1, my1))
heapq.heappush(q, (0, 2, mx1, my1))
heapq.heappush(q, (0, 3, mx1, my1))

while q:
    cnt, direction, x, y = heapq.heappop(q)
    if x == mx2 and y == my2:
        ans = min(ans, cnt)
    else:
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':
                if i != direction:
                    if visited[nx][ny] >= cnt + 1:
                        visited[nx][ny] = cnt + 1
                        heapq.heappush(q, (cnt + 1, i, nx, ny))
                else:
                    if visited[nx][ny] >= cnt:
                        visited[nx][ny] = cnt
                        heapq.heappush(q, (cnt, i, nx, ny))

print(ans)