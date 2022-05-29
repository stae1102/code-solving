import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))
a = [data[0]]

for x in data[1:]:
    if x[0] >= a[-1][1]:
        a.append(x)

print(len(a))