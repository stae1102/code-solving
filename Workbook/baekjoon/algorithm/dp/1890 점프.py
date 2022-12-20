import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(d[i][j])
            break
        move = graph[i][j]
        if i + move < n:
            d[i + move][j] += d[i][j]
        if j + move < n:
            d[i][j + move] += d[i][j]