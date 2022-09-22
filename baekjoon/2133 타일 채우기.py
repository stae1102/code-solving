d = [0] * 31

d[0] = 1

n = int(input())

for i in range(2, n + 1):
    d[i] = d[i - 2] * 3
    for j in range(4, n + 1, 2):
        d[i] += d[i - j] * 2

print(d[n])
