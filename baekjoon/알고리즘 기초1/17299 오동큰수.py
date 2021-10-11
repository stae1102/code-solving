import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []
ans = [-1] * len(arr)
cnt = {}

for i in arr:
    cnt[i] = cnt.get(i, 0) + 1

for i in range(len(arr) - 1, -1, -1):
    while stack and cnt[stack[-1]] <= cnt[arr[i]]:
        stack.pop()
    if not stack:
        stack.append(arr[i])
    else:
        ans[i] = stack[-1]
        stack.append(arr[i])

print(' '.join(map(str, ans)))
