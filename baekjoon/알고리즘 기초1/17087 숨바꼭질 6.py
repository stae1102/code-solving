import sys
import math
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(len(arr)):
    arr[i] = abs(arr[i] - s)

num = arr[0]
for i in range(1, len(arr)):
    num = math.gcd(arr[i], num)
print(num)
