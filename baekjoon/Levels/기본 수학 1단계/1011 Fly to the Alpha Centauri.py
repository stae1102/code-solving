import sys
input = sys.stdin.readline

for i in range(int(input())):
    x, y = map(int, input().split())
    dis = y - x  # 거리
    k = 0 # 가장 높은 곳의 값
    answer = 0
    while True: # k 값 구하기
        k += 1
        if k ** 2 <= dis < (k + 1) ** 2:
            break
    if dis - (k ** 2) == 0:
        answer = k * 2 - 1
    elif 0 < dis - (k ** 2) <= k:
        answer = k * 2
    else:
        answer = k * 2 + 1
    print(answer)
