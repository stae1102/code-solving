import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = [(0, 1), (1, 0), (-1, 0)]
ans, MAX = 0, max(map(max, graph))

def dfs(x, y, cnt, SUM):
    global ans
    if cnt == 0:
        ans = max(ans, SUM)
        return

    if ans >= SUM + cnt * MAX:
        return

    for i, j in move:
        nx = x + i
        ny = y + j
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            if cnt == 2:
                dfs(x, y, cnt - 1, SUM + graph[nx][ny])
            dfs(nx, ny, cnt - 1, SUM + graph[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 3, graph[i][j])
        visited[i][j] = 0

print(ans)