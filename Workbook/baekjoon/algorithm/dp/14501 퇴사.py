import sys
input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

d = [0] * N

for i in range(N):
    if i + arr[i][0] - 1 < N:
        d[i + arr[i][0] - 1] = max(d[i + arr[i][0] - 1], arr[i][1] + d[i - 1])
    if i > 0:
        d[i] = max(d[i], d[i - 1])

print(d[-1])