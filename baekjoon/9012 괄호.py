from sys import stdin

n = int(stdin.readline())

def solve(arr):
    cnt = len(arr)
    stack = []
    for i in range(cnt):
        if arr[i] == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
    return "YES" if len(stack) == 0 else "NO"

for _ in range(n):
    ps = stdin.readline().rstrip()
    tof = solve(ps)
    print(tof)