from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_prisoner():
    prisoner = []

    jail = [['.'] * (w + 2)]
    for _ in range(h):
        row = list('.' + input().rstrip() + '.')
        jail.append(row)
    jail.append(['.'] * (w + 2))

    for i in range(h + 2):
        for j in range(w + 2):
            if jail[i][j] == '$':
                prisoner.append((i, j))
    
    return prisoner, jail

def bfs(arr):
    x, y = arr
    q = deque([(x, y)])
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and visited[nx][ny] == -1:
                if jail[nx][ny] == '.' or jail[nx][ny] == '$':
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                elif jail[nx][ny] == '#':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return visited


for _ in range(T):
    h, w = map(int, input().split())
    prisoner, jail = get_prisoner()
    first = bfs(prisoner[0])
    second = bfs(prisoner[1])
    zero = bfs((0, 0))
    ans = float('inf')

    for i in range(h + 2):
        for j in range(w + 2):
            if not(first[i][j] == -1 or second[i][j] == -1 or zero[i][j] == -1):
                if jail[i][j] != '*':
                    result = first[i][j] + second[i][j] + zero[i][j]
                    if jail[i][j] == '#':
                        result -= 2
                    ans = min(ans, result)

    print(ans)