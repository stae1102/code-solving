import sys
strs = sys.stdin.readline().rstrip()
ptr = 0
ans = []
temp = ""

while ptr < len(strs): # split() 함수를 새로 구현
    if strs[ptr] == "<": # "<"를 만났을 때
        if temp: # 여태 나왔던 문자열을 저장함
            ans.append(temp)
        temp = "" # 문자열 초기화
        left = ptr
        while strs[ptr] != ">": # <>가 완성될 때까지
            ptr += 1
        ans.append(strs[left : ptr + 1]) # 여태 나온 것들을 토대로 append
        ptr += 1 # 그 다음부터 출발
        continue # 인덱싱에서 IndexError가 발생할 수 있으니 continue 필수
    temp += strs[ptr]
    ptr += 1 # 포인터 계속 이동
    # print(ans)
else:
    ans.append(temp) # 문자열로만 구성되어 있거나, 문자열로 끝나는 경우에 append를 다시 해줘야 함

for i in ans:
    if "<" in i:
        print(i, end="") # "<" 가 들어 있으면 tag로 판단
    else:
        rvs = i[::-1].split()
        rvs.reverse()
        rvs = ' '.join(rvs)
        print(rvs, end="") # 문자열 부분은 거꾸로 출력
        
#### 모범 답안 ####

a = input()
b = a.replace('>','<').split('<')
s = ""

for i in range(len(b)):
    if i % 2:
        s += "<" + b[i] + ">"
    else:
        c = b[i].split()
        s += ' '.join(d[::-1] for d in c)
print(s)

"""
        태그와 태그 사이에 문자가 존재 => 태그는 짝이 있음
        즉, 태그를 split했을 때, 홀수 인덱스는 무조건 태그임
        이를 위해서 문자열을 replace를 통해 전처리를 해주었고
        < 를 통해 나누었음.
"""
