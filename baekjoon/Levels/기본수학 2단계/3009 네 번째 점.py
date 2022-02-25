x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    if a in x:
        x.remove(a)        # 이미 값이 있으면 제거
    else:
        x.append(a)
    if b in y:
        y.remove(b)        # 이미 값이 있으면 제거
    else:
        y.append(b)

print(*x, *y)

