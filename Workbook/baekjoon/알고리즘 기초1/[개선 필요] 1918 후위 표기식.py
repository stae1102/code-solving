string = list(input())

stack = []    # 괄호를 저장하는 스택
val = {"+" : 1, "-" : 1, "*" : 2, "/" : 2} # 연산자의 우선순위
oper = []      # 연산자를 저장할 리스트

ans = []      # 후위 표기식

for i in string:
    if i in ["+", "-", "*", "/"]:
        if not oper:
            oper.append([i, len(stack)])
        elif len(stack) == oper[-1][1]:
            if val[i] > val[oper[-1][0]]:         # 추가 연산자의 우선순위가 이전보다 클 때
                oper.append([i, len(stack)])
            else:
                ans.append(oper.pop()[0])    # 추가 연산자의 우선순위가 이전보다 적을 때
                if oper and val[i] == val[oper[-1][0]] and len(stack) == oper[-1][1]:
                    ans.append(oper.pop()[0])
                    oper.append([i, len(stack)])
                    continue
                oper.append([i, len(stack)])
        else:
            oper.append([i, len(stack)])
    elif i == "(":
        stack.append(i)
    
    elif i == ")":
        stack.pop()
        if oper and len(stack) == oper[-1][1]:
            ans.append(oper.pop()[0])
        while oper:
            if oper[-1][1] == len(stack) + 1:
                ans.append(oper.pop()[0])
            else:
                break
    else:
        ans.append(i)

while oper:
    ans.append(oper.pop()[0])

print(''.join(ans))
