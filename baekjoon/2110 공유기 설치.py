import sys

n, c = map(int, sys.stdin.readline().split())
x = sorted(map(int, sys.stdin.readlines()))

# 거리를 이진탐색으로 정하고, for문으로 0 인덱스로부터 검사하기 시작.
# 만약 검사하면서 가능한 경우가 c보다 작으면 거리를 줄임
# 가능한 경우가 c보다 크다면 거리를 넓힘(이때 ans 저장)

pl, pr = 1, x[-1] - x[0]
dist = 0

while pl <= pr:
    mid = (pl + pr) // 2
    standard = x[0]
    available = 1

    for i in range(1, n):
        if x[i] - standard >= mid:
            standard = x[i]
            available += 1

    if available >= c:
        dist = mid
        pl = mid + 1
    else:
        pr = mid - 1

print(dist)
