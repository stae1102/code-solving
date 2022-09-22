import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

pl, pr = 0, max(trees)
ans = 0

while pl <= pr:
    mid = (pl + pr) // 2
    tmp = 0
    for tree in trees:
        if tree > mid:
            tmp += tree - mid
    if tmp < m:
        pr = mid - 1
    else:
        pl = mid + 1
        ans = mid

print(ans)
