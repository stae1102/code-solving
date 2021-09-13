# 시간초과 코드1

a = int(input())
b = list(map(int, input().split()))
stack = []

for i in b[::-1]:
    if b.index(i) == 0:
        stack.append(0)
        break
    for j in b[b.index(i) - 1::-1]:
        if j > i:
            stack.append(b.index(j) + 1)
            break
    else: stack.append(0)
stack = reversed(stack)
print(' '.join(map(str, stack)))

# 시간 초과 코드2
a = int(input())
stack = list(map(int, input().split())) # 정수형으로 스택을 생성
new_stack = []

# pop()으로 꺼내며 수를 비교
for i in range(a):
    pop = stack.pop()
    for j in reversed(stack):
        if j >= pop:
            new_stack.append(stack.index(j) + 1)
            break
    else: new_stack.append(0)
new_stack = ' '.join(map(str, reversed(new_stack)))
print(new_stack)

# 정답 코드

a = int(input())
b = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(a)]
for i in range(a):
    while stack:
        if stack[-1][1] > b[i]:
            answer[i] = stack[-1][0] + 1
            break
        else: stack.pop()
    stack.append([i, b[i]])
print(*answer)
