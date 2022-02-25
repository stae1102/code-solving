import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]    # 코인들을 입력
count = 0                                   # 총 사용된 코인 수를 받을 객체 생성

for i in range(len(coins) - 1, -1, -1):     # 큰 값의 동전부터 사용
    if coins[i] > k:                        # 남은 동전보다 크면 멈춤
        continue
    count += k // coins[i]                  # 몫을 count에 더해서 사용된 동전 계산
    k %= coins[i]                           # 남은 금액

print(count)
