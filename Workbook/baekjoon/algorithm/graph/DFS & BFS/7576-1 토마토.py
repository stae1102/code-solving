from collections import deque
import sys
input = sys.stdin.readline

'''
M: 상자의 가로 칸 수
N: 상자의 세로 칸 수
'''

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    days = 0
    q = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                days += 1
            elif graph[i][j] == 1:
                q.append((i, j, 0))
    
    if days == 0:
        return 0
    
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    days -= 1
                    if days == 0:
                        return cnt + 1
                    q.append((nx, ny, cnt + 1))

    return -1

print(bfs())