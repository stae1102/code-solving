import sys
import math
input = sys.stdin.readline
INF = math.inf

n, m = map(int, input().split())

array = list(map(int, input().split()))

left = 0
right = 0
interval_sum = 0
length = INF

while left <= right and right < n:
    while right < n:
        interval_sum += array[right]
        if interval_sum >= m:
            break
        right += 1

    while left <= right:
        if interval_sum < m:
            break
        interval_sum -= array[left]
        length = min(length, right - left + 1)
        left += 1
    right += 1

if length != INF:
    print(length)
else:
    print(0)