import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())

left_center = [x, y + h // 2]
right_center = [x + w, y + h // 2]

ans = 0
for _ in range(p):
    px, py = map(int, input().split())
    dist1 = (px - left_center[0]) ** 2 + (py - left_center[1]) ** 2
    dist2 = (px - right_center[0]) ** 2 + (py - right_center[1]) ** 2
    if (dist1 <= (h // 2) ** 2 or dist2 <= (h // 2) ** 2) or ((x <= px <= x + w) and (y <= py <= y + h)):
        ans += 1
print(ans)