import sys
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N + 1)]
arr[1:] = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * i for i in range(N + 1)]
d[1] = arr[1]

for i in range(1, N):
    for j in range(len(arr[i])):
        d[i + 1][j] = max(d[i + 1][j], d[i][j] + arr[i + 1][j])
        d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + arr[i + 1][j + 1])

print(max(d[N]))