n = int(input())

d = [i for i in range(n + 1)]

for i in range(2, int(n ** 0.5) + 1):
    j = i ** 2
    k = i ** 2
    d[j] = 1
    while k <= n:
        d[k] = min(d[k], d[k - j] + 1)
        k += 1

print(d[n])