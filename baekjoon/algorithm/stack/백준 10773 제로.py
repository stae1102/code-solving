import sys
a = int(sys.stdin.readline().strip())
stack = []

for i in range(a):
    b = int(sys.stdin.readline().strip())
    if b:
        stack.append(b)
    else:
        stack.pop()

print(sum(stack))
