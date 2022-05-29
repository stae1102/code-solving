from collections import deque
import sys
input = sys.stdin.readline

while True:
    n, *arr = map(int, input().split())
    
    if n == 0:
        break

    ans = -1
    stack = deque()
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            idx = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1

            ans = max(ans, width * arr[idx])
        stack.append(i)

    while len(stack) != 0:
        idx = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1

        ans = max(ans, width * arr[idx])
    
    print(ans)