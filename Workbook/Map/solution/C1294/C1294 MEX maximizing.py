import sys
input = sys.stdin.readline
q, x = map(int, input().split())
map = {}
mex = 0

for i in range(q):
    y = int(input())
    if y % x in map:
        if y % x + x * map[y % x] in map:
            map[y % x + x * map[y % x]] += 1
        else:
            map[y % x + x * map[y % x]] = 1
        map[y % x] += 1
    else:
        map[y % x] = 1
    
    while mex in map:
        mex += 1
    print(mex)