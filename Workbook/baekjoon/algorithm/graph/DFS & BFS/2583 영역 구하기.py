from collections import deque
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())

# 이동방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 구현
def bfs(x, y):
    # 이미 칠해져 있으면 0 반환
    if graph[x][y] == 1:
        return 0
    q = deque([(x, y)])
    graph[x][y] = 1
    cnt = 0
    # 본격적으로 넓이 채우기
    while q:
        x, y = q.popleft()
        # 현재의 위치가 비어있었기 때문에 +1
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 탐색이 범위 안에 있을 때,
            if 0 <= nx < n and 0 <= ny < m:
                # 범위 안에 있으며 비어 있는 곳일 때 
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny))
    
    return cnt


graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        graph[i][y1:y2] = [1] * (y2 - y1)

ans = []

for a in range(n):
    for b in range(m):
        s = bfs(a, b)
        if s > 0:
            ans.append(s)

print(len(ans))
print(*sorted(ans))
