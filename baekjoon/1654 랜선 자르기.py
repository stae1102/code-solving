import sys

n, k = map(int, sys.stdin.readline().split())

lans = list(map(int, sys.stdin.readlines()))

pl, pr = 1, max(lans)
ans = 0

while pl <= pr:
    mid = (pl + pr) // 2
    tmp = 0

    for lan in lans:
        tmp += lan // mid

    if tmp < k:
        pr = mid - 1
    else:
        pl = mid + 1
        ans = mid

print(ans)
