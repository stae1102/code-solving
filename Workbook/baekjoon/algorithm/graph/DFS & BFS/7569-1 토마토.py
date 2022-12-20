from collections import deque
import sys
input = sys.stdin.readline

'''
M: 상자의 가로 칸 수
N: 상자의 세로 칸 수
H: 쌓아 올려지는 상자의 수
'''
M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]

# 이동 범위
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 3차원 리스트 활용
for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

def bfs():
    q = deque()
    days = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    days += 1
                elif graph[i][j][k] == 1:
                    q.append((i, j, k, 0))
    
    if days == 0:
        return 0

    while q:
        x, y, z, cnt = q.popleft()
        for i in range(6):
            nx = x + dx[i]; ny = y + dy[i]; nz = z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = 1
                    days -= 1
                    if days == 0:
                        return cnt + 1
                    q.append((nx, ny, nz, cnt + 1))
    
    return -1

print(bfs())