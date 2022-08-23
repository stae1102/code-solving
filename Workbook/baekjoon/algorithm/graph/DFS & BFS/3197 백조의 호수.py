from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
swan = deque()
next_swan = deque()
water = deque()
ice = deque()

for i in range(r):
    row = list(input().rstrip())
    for a, b in enumerate(row):
        if b != 'X':
            if b == 'L':
                swan.append([i, a])
            water.append((i, a))
    graph.append(row)

swan[0].append('L1')
swan[1].append('L2')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0] * c for _ in range(r)]
visited_s = [[0] * c for _ in range(r)]

def melt():
    
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 'X':
                    graph[nx][ny] = '.'
                    ice.append((nx, ny))
                    continue
                # water.append((nx, ny))

def find_swan():

    while swan:
        x, y, l = swan.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (l == 'L1' and graph[nx][ny] == 'L2') or (l == 'L2' and graph[nx][ny] == 'L1'):
                    return True
                if not visited_s[nx][ny]:
                    if graph[nx][ny] == 'X':
                        next_swan.append((x, y, l))
                        continue
                    visited_s[nx][ny] = 1
                    graph[nx][ny] = l
                    swan.append((nx, ny, l))

    return False

ans = 0

while True:
    if find_swan():
        print(ans)
        exit()
    melt()
    swan, next_swan = next_swan, swan
    water, ice = ice, water
    ans += 1