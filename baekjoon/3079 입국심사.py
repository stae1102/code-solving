import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = [int(input()) for _ in range(n)]

pl, pr = 1, m * max(s)
ans = 0

while pl <= pr:
    mid = (pl + pr) // 2
    total = sum(map(lambda x: mid // x, s))

    if total >= m:
        pr = mid - 1
        ans = mid
    else:
        pl = mid + 1


print(ans)
