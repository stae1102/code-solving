n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 2
div = 10007

for i in range(3, n + 1):
    d[i] = d[i - 1] % div + d[i - 2] % div
    d[i] %= div

print(d[n])
