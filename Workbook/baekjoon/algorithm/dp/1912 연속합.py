import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = arr[0]

for i in range(1, N):
    arr[i] = max(arr[i - 1] + arr[i], arr[i])
    ans = max(ans, arr[i])
    
print(ans)