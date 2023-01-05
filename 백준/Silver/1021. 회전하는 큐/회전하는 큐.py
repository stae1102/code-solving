from collections import deque
n, m = map(int, input().split())
arr = deque([i for i in range(1, n + 1)])
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
  while True:
    if arr[0] == num:
      arr.popleft()
      break
    if arr.index(num) <= len(arr) // 2:
        arr.append(arr.popleft())
        cnt += 1
    else:
        arr.appendleft(arr.pop())
        cnt += 1

print(cnt)