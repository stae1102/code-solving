import sys
input = sys.stdin.readline
sys.setrecursionlimit(2503)
t = int(input())

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(j, i) == True:
                result += 1
    print(result)
