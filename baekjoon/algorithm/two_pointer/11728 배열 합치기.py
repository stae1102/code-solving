n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')