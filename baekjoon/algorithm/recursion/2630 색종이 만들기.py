from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]    # 배열 설정
white, black = 0, 0    # 색종이 색깔 설정

to_do = deque([[0, 0, n]])    # 큐 설정
while to_do:
    x, y, n = to_do.popleft()
    sub = 0
    # 해당 색종이 변의 합
    for i in range(x, x + n):
        for j in range(y, y + n):
            sub += arr[i][j]
    # 모두 흰 색이면
    if sub == 0:
        white += 1
    # 모두 검은 색이면
    elif sub == n ** 2:
        black += 1
    # 섞여 있으면
    else:
        to_do.append([x, y, n // 2])
        to_do.append([x + n // 2, y, n // 2])
        to_do.append([x, y + n // 2, n // 2])
        to_do.append([x + n // 2, y + n // 2, n // 2])

print(white)
print(black)
