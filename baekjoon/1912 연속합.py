import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]

for i in range(1, n):
    arr[i] = max(arr[i - 1] + arr[i], arr[i])
    ans = max(ans, arr[i])

print(ans)
