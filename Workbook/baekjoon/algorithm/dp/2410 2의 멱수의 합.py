d = [0] * 1000001
d[1] = 1
d[2] = 2
d[3] = 2

for i in range(4, 1000001):
    if i % 2 == 0:
        d[i] = (d[i - 1] + d[i // 2]) % 1000000000
    else:
        d[i] = d[i - 1]

n = int(input())

print(d[n])