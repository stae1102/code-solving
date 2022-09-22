import sys
import heapq
input = sys.stdin.readline


def dijkstra(x, y):
    q = []
    heapq.heappush(q, (x, y))
    dist[0][0] = graph[0][0]

    while q:
        x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                    dist[nx][ny] = dist[x][y] + graph[nx][ny]
                    heapq.heappush(q, (nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]

    dijkstra(0, 0)
    print(f"Problem {cnt}: {dist[-1][-1]}")
