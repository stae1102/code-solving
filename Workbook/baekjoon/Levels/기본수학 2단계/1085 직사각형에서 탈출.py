x, y, w, h = map(int, input().split())
sub_1 = w - x # 지점과 오른쪽 벽
sub_2 = h - y # 지점과 위쪽 벽
min1 = sub_1 if sub_1 <= sub_2 else sub_2
min2 = x if x <=y else y
print(min1) if min1 <= min2 else print(min2)
