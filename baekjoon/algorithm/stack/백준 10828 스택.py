######################## 첫 번쨰 코드(시간 초과) ########################
# 스택 프로그램 제작
n = int(input()) # 명령 수 지정
stack = []

for i in range(n):
    command = list(input().split())
    if 'push' in command:
        stack.append(command[-1])
    elif 'pop' in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
            
######################## 두 번째 코드(성공) ########################
import sys
n = int(sys.stdin.readline().strip())
stack = []
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if 'push' in command: stack.append(command[-1])
    elif 'pop' in command:
        if stack: print(stack.pop())
        else: print(-1)
    elif 'size' in command: print(len(stack))
    elif 'empty' in command:
        if stack: print(0)
        else: print(1)
    else:
        if stack: print(stack[-1])
        else: print(-1)
