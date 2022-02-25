# 백준 1874 스택 수열
import sys
a = int(sys.stdin.readline().strip()) # 반복 횟수
stack = [1] # 스택에 먼저 1을 넣어줌 (어차피 반드시 1로 시작함)
answer = 1 # 시도 횟수
output = ['+']
b = int(sys.stdin.readline().strip()) # 먼저 전역 변수를 설정

while answer != a + 1:
    if (len(stack) == 0) or stack[-1] < b: # 비어있을 때, -1 인덱스를 찾으면 오류가 발생하기 때문에 or 그리고 len(stack) == 0을 이용함
        answer += 1 # top이 입력값보다 작기 때문에 계속해서 수를 늘리며 push해줌
        stack.append(answer)
        output.append('+')
    elif stack[-1] == b: # 설정값에 다다르면 pop을 통해 꺼내줌
        stack.pop()
        output.append('-')
        if answer == a and not stack: # 만약 스택에 쓰일 숫자를 다 쓰고, 스택이 비어있다면 탈출
            break
        b = int(sys.stdin.readline().strip())
    else:
        output.append(-1) # top이 입력값보다 크다면 그것은 수열이 불가능하기 때문에 예외 적용
        print("NO")
        break
    
if -1 not in output: # output에 -1이 없어야 수열을 만들 수 있는 것이기 때문에
    print(*output, sep='\n')
