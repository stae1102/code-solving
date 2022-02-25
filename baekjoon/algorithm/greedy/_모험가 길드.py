import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()

cost = 0
group = 0

for i in l:
    cost += 1
    if cost >= i:
        group += 1
        cost = 0

print(group)
