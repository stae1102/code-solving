def traverse_left(arr, n):
  dp = [1] * n
  for i in range(1, n):
    for j in range(i):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)
    
  return dp

def traverse_right(arr, n):
  dp = [1] * n
  for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  
  return dp

n = int(input())
arr = list(map(int, input().split()))

dp_left = traverse_left(arr, n)
dp_right = traverse_right(arr, n)

dp = [a + b for a, b in zip(dp_left, dp_right)]

print(max(dp) - 1)