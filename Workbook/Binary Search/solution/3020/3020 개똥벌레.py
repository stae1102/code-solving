import sys
input = sys.stdin.readline

def lower_bound(s, e, d, L):
    while s < e:
        mid = (s + e) // 2
        if L[mid] < d:
            s = mid + 1
        else:
            e = mid
    return e

up = []
down = []
result = [0] * 500001
n, h = map(int, input().split())

for i in range(n):
    x = int(input())
    if i % 2:
        up.append(x)
    else:
        down.append(x)

up.sort()
down.sort()

ans = 0
MIN = float('inf')

for i in range(1, h + 1):
    idxd = lower_bound(0, len(down), i, down)
    idxu = lower_bound(0, len(up), h - i + 1, up)
    result[i] = n // 2 - idxd + n // 2 - idxu
    MIN = min(MIN, result[i])

for i in range(1, h + 1):
    if result[i] == MIN:
        ans += 1

print(MIN, ans)