# 쇠막대기에 필요한 것은 / 전체 스택, 스캔기능
# 스택에 리스트를 추가시켜서, 괄호와 그 괄호의 인덱스 숫자도 포함
# 레이저에 스캔기능을 포함하여 len(stack)을 통해 전체 스냅샷 초기화
n = input()
stack = []
answer = []
snap = 0
count = 0 

for i in n:
    count += 1
    if i == "(":
        stack.append([i, count])
        snap += 1
    else: # ")"인 경우
        if stack[-1][1] == count - 1: # 마지막이 "("이고 바로 앞 인덱스인 경우
            stack.pop()
            snap -= 1
            answer.append(snap)
            snap = len(stack)
        else:
            stack.pop()
else:
    answer.append(snap) # 어차피 마지막 레이저 뒤 부분은 이전 쇠막대의 개수와 동일하기 때문에 스냅샷을 한 번 더 더해줌
print(sum(answer))
