import sys
r = sys.stdin.readline

n = int(r())

arr = list(map(int, r().split()))
visited = [False] * n
ans = [0] * n

max_val = 0

def calc(depth):
    global max_val
    if depth == n:
        temp = 0
        for i in range(n - 1):
            temp += abs(ans[i] - ans[i + 1])
        max_val = max(max_val, temp)
        return

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        ans[depth] = arr[i]
        calc(depth + 1)
        visited[i] = False

calc(0)

print(max_val)