import sys
input = sys.stdin.readline
t, w = map(int, input().split())

d = [[0] * (w + 1) for _ in range(t)]
tree = [[0, 0] for _ in range(t)]

for i in range(t):
    k = int(input())
    tree[i][k - 1] += 1

d[0][0] = tree[0][0]; d[0][1] = tree[0][1]

for i in range(1, t):
    d[i][0] = d[i-1][0] + tree[i][0]
    for j in range(1, w + 1):
        d[i][j] = max(d[i-1][j-1], d[i-1][j]) + tree[i][j % 2]

print(max(d[-1]))