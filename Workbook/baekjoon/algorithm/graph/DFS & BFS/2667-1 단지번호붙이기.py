from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return cnt

result = []
for a in range(N):
    for b in range(N):
        if graph[a][b] and not visited[a][b]:
            result.append(bfs(a, b))

print(len(result))
for i in sorted(result):
    print(i)