n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

s = 0
m = 1e9

for d, c in zip(dist, cost[:-1]):
    if c < m:
        m = c
    s += d * m

print(s)
