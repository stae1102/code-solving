n = int(input())

tmp = ["SK", "CY"]
d = [-1] * 1001

d[1] = 0
d[2] = 1
d[3] = 0
d[4] = 0

for i in range(5, n + 1):
    if d[i - 1] == d[i - 3] == d[i - 4] == 0:
        d[i] = 1
    else:
        d[i] = 0

print(tmp[d[n]])
