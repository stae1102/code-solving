import sys
n = int(sys.stdin.readline())
cal = sys.stdin.readline().rstrip()
nums = {}
stack = []

for i in [chr(64 + s) for s in range(1, n + 1)]:
    nums[i] = int(sys.stdin.readline())

for i in cal:
    if i in ["+", "-", "*", "/"]:
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            exp = b + a
        elif i == "-":
            exp = b - a
        elif i == "*":
            exp = b * a
        else:
            exp = b / a
        stack.append(exp)
        continue
    stack.append(nums[i])
print(f'{stack.pop():.2f}')
