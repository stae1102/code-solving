n = int(input())
d = [0, 1, 2, 3]

for i in range(4, n + 1):
    d.append(i)
    k = 2
    while k ** 2 <= i:
        d[i] = min(d[i], d[i - k ** 2] + 1)
        k += 1

print(d[n])
