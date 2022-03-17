import sys
import math
input = sys.stdin.readline
INF = math.inf

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

start, end = 0, 1
result = INF

while start <= end < n:
    diff = arr[end] - arr[start]
    if diff >= m:
        result = min(result, diff)
        start += 1
    elif end == n:
        break
    else:
        end += 1

print(result)