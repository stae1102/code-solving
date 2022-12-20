import sys
n = int(sys.stdin.readline())
cnt = 0

for a in range(1, 501):
    for b in range(1, 501):
        if a ** 2 == b ** 2 + n:
            cnt += 1
        if a ** 2 < b ** 2 + n:
            break

print(cnt)