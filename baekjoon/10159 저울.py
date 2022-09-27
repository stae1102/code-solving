import sys
input = sys.stdin.readline
INF = float('inf')
n = int(input())

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 1

m = int(input())

# i > j는 1로, i < j는 -1로 정의하여 방향을 잡음
for _ in range(m):
    i, j = map(int, input().split())
    distance[i][j] = 1
    distance[j][i] = -1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if distance[a][k] == distance[k][b] != INF:
                distance[a][b] = distance[a][k]

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            cnt += 1
    print(cnt)
