import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

s = 0
m = 987654321

for d, c in zip(road, city[:-1]):
    if c < m:
        m = c
    s += d * m

print(s)
