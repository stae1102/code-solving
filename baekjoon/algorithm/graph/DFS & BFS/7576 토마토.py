from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [(list(map(int, input().rstrip().split()))) for _ in range(n)]
do = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            do += 1
        elif tomato[i][j] == 1:
            queue.append((i, j))

result = 0
while queue and do:
    result += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = 1
                do -= 1

if do:
    print(-1)
else:
    print(result)
