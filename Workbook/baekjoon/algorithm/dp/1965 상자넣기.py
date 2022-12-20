n = int(input())

box = list(map(int, input().split()))
d = [0 for _ in range(n)]
d[0] = 1
ans = 0

for i in range(1, n):
    for j in range(0, i):
        if box[j] < box[i]:
            d[i] = max(d[i], d[j])
    d[i] += 1
    ans = max(ans, d[i])

print(ans)