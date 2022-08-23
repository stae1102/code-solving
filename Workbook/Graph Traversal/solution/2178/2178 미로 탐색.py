from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 큐 생성
q = deque([(0, 0)])

# BFS 알고리즘
while q:
    x, y = q.popleft()

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1: # 방문 가능한 곳일 때
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny)) # 다음으로 갈 곳

print(graph[N-1][M-1])