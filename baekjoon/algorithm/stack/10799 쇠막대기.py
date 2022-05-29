metal = input()
stack = []
answer = 0
for i in range(len(metal)):
    if metal[i] == '(':
        stack.append(metal[i])
    else:
        stack.pop()
        if metal[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1
print(answer)