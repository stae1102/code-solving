import sys
strs = list(sys.stdin.readline().rstrip())
ptr = len(strs)
stack = []

for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().rstrip()
    if "L" == cmd and strs:
        stack.append(strs.pop())
    elif "D" == cmd and stack:
        strs.append(stack.pop())
    elif "B" == cmd and strs:
        strs.pop()
    elif "P" in cmd:
        strs.append(cmd.split()[1])

print(''.join(strs + stack[::-1]))

"""
스택을 하나 더 만들어서 이중 스택
    [    "ptr"    ]
    ↑    포인터   ↑
왼쪽 스택     오른쪽 스택
L이면 포인터가 왼쪽으로 이동하기 때문에 왼쪽 스택의 pop 값을 오른쪽에 append해줌.
D도 마찬가지,
B는 pop
P는 커서 왼쪽에 삽입하기 때문에 왼쪽 스택에 append
"""
