n = int(input())

cnt = 0

for b in range(1, n - 1):
    for c in range(b + 2, n - b - 1):
        if (n - b - c) % 2 == 0:
            cnt += 1

print(cnt)