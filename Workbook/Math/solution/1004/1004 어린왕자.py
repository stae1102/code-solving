import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        if (dist1 <= r ** 2 and dist2 > r ** 2) or (dist1 > r ** 2 and dist2 <= r ** 2):
            ans += 1
    print(ans)