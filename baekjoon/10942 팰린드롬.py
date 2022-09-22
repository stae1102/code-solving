import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(pl, pr):
    if arr[pl] != arr[pr]:
        return 0
    if d[pl][pr] or pl > pr:
        return 1

    d[pl][pr] = find(pl + 1, pr - 1)
    return d[pl][pr]


n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

d = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][i] = 1
    for j in range(i + 1, n + 1):
        d[i][j] = find(i, j)

for _ in range(m):
    s, e = map(int, input().split())
    print(d[s][e])
