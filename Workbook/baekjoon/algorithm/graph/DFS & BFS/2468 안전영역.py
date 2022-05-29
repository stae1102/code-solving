import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(x, y):
    if 0 <= x < n and 0 <= y < n and temp[x][y] > h:
        temp[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

n = int(input())

hgt = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    hgt.append(list(map(int, input().split())))

rain = [1] + [0] * 100

for h in range(1, 101):
    temp = [[i for i in hgt[j]] for j in range(n)]
    for a in range(n):
        for b in range(n):
            if temp[a][b] > h:
                rain[h] += 1
                dfs(a, b)
    if rain[h] == 0:
        break

print(max(rain))
