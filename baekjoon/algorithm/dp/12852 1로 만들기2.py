import sys
input = sys.stdin.readline

N = int(input())

d = [0] * (N + 1)

for i in range(2, N + 1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

arr = []
ans = 0

while N != 0:
    arr.append(N)
    temp = N
    MIN = d[temp-1]
    N = temp - 1

    if temp % 2 == 0 and temp >= 2:
        if MIN >= d[temp//2]:
            MIN = d[temp//2]
            N = temp // 2

    if temp % 3 == 0 and temp >= 3:
        if MIN >= d[temp//3]:
            MIN = d[temp//3]
            N = temp // 3

    ans += 1

print(ans - 1)
print(*arr)