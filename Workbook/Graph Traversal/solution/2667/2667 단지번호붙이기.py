from collections import deque
import sys
input = sys.stdin.readline

'''
1. Use the for loop
2. if graph[i] is "0", ignore and skip to next
3. if graph[i] is "1", do the BFS algorithm
'''

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# Define directions
# Up, Down, Left, Right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS algorithm

def bfs(x, y):
    graph[x][y] = 0
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))

    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans), sep="\n")