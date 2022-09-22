import sys

n = int(sys.stdin.readline())
stairs = list(map(int, ['0'] + sys.stdin.readlines()))

g = [0, 0]
h = [0, stairs[1]]

for i in range(2, n + 1):
    g.append(h[i - 1] + stairs[i])
    h.append(max(g[i - 2], h[i - 2]) + stairs[i])

print(max(g[n], h[n]))
