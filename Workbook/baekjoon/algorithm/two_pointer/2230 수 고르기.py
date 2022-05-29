import sys
import math
input = sys.stdin.readline
INF = math.inf

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

end = 0
diff = math.inf

for i in range(n):
    while end < n and (arr[end] - arr[i] < m):
        end += 1
    
    if end < n:
        diff = min(diff, arr[end] - arr[i])

print(diff)