import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (n + 1)] + [[0] + list(map(int, input().split()))
                           for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        graph[i][j] += graph[i][j - 1]

for _ in range(m):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2 + 1):
        ans += graph[x][y2] - graph[x][y1 - 1]

    print(ans)
