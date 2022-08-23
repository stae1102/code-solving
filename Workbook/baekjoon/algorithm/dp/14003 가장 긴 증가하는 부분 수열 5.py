from collections import deque
import bisect
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
s = [-1000000001]
MAX = 0

for i in range(1, n + 1):
    if s[-1] < arr[i]:
        s.append(arr[i])
        d[i] = len(s) - 1
        MAX = d[i]
    else:
        d[i] = bisect.bisect_left(s, arr[i])
        s[d[i]] = arr[i]

print(MAX)

r = deque([])
for i in range(n, 0, -1):
    if d[i] == MAX:
        r.appendleft(arr[i])
        MAX -= 1

print(*r)