import sys
input = sys.stdin.readline

n = int(input())
provinces = list(map(int, input().split()))
m = int(input())

pl, pr = 1, max(provinces)
ans = 0

while pl <= pr:
    mid = (pl + pr) // 2
    temp = 0
    for province in provinces:
        if mid > province:
            temp += province
        else:
            temp += mid

    if temp <= m:
        pl = mid + 1
        ans = mid
    else:
        pr = mid - 1

print(ans)
