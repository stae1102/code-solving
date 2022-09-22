import sys
import heapq
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]


def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    dist[x][y] = 0
    while q:
        x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (dist[nx][ny] > dist[x][y] + graph[nx][ny]):
                    dist[nx][ny] = dist[x][y] + graph[nx][ny]
                    heapq.heappush(q, (dist[nx][ny], nx, ny))


dijkstra(0, 0)

print(dist[-1][-1])
