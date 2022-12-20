from sys import stdin
input = stdin.readline

area = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if area[i][j] == 0:
                ans += 1
            area[i][j] += 1

print(ans)
