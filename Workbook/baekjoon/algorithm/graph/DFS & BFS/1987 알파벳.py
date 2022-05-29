def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if -1 < nx < r and -1 < ny < c and alphabet[graph[nx][ny]] == 0:
            alphabet[graph[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            alphabet[graph[nx][ny]] = 0

import sys
r, c = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append(list(map(lambda a: ord(a) - 65, sys.stdin.readline().rstrip())))

alphabet = [0] * 26
alphabet[graph[0][0]] = 1

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
result = 0
dfs(0, 0, 1)
print(result)
