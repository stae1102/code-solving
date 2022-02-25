import sys
k, n = map(int, sys.stdin.readline().split())
l = []

for i in range(k):
    l.append(int(sys.stdin.readline()))

pl, pr = 1, max(l)

while pl <= pr:
    mean = (pl + pr) // 2
    ans = 0
    for i in l:
        ans += i // mean
    
    if ans < n:
        pr = mean - 1
    else:
        pl = mean + 1

print(pr)
