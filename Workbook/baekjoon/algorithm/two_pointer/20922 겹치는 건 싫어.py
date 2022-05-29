import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = [0] * (n + 1)
array[1:] = list(map(int, input().split()))

# counting 변수 생성
count = [0] * 100001
length = 0

# [left, right]로 구역을 설정.
# right를 1씩 늘려가다가 카운트가 m을 넘어서면 left를 늘려감.
# 매번 max를 갱신함

left, right = 1, 1
while left <= right and right <= n:
    while (right <= n and count[array[right]] <= m):
        if count[array[right]] == m:
            break
        count[array[right]] += 1
        length = max(length, right - left + 1)
        right += 1
    
    while left < right:
        if (count[array[left]] == m):
            count[array[left]] -= 1
            left += 1
            break

        count[array[left]] -= 1
        left += 1

print(length)