import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))
a = [data[0]]

for x in data[1:]:
    if x[0] >= a[-1][1]:
        a.append(x)

print(len(a))

############################
########### 모범 ###########
############################

import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    dic = {}
    for _ in range(N):
        start, end = map(int, input().split())
        if dic.get(start):
            dic[start].append(end)  # min(dic.get(start, float('inf')), end)
        else:
            dic[start] = [end]
    
    for k in dic.keys():
        dic[k].sort()
        
    keys = sorted(dic.keys())
    end = 0
    count = 0
    print(keys)
    for key in keys:
        for e in dic[key]:
            print(dic[key], e)
            if e < end:
                end = e
            elif key >= end:
                count += 1
                end = e

    print(count)


solve()
