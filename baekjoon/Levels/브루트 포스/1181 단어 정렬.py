########## 첫 번째 방법(실패) ##########

import sys
input = sys.stdin.readline
n = int(input())

s = []

for i in range(n):
    str_ = input().rstrip()
    s.append([str_ , len(str_)])

h = n // 2

while h > 0:
    for i in range(h, n):
        j = i - h
        tmp = s[i]
        while j >= 0 and s[j][1] > tmp[1]:
            s[j + h] = s[j]
            j -= h
        s[j + h] = tmp
    h //= 2

for i in range(1, n):
    j = i
    tmp = s[i]
    while j > 0 and s[j - 1][0] > tmp[0] and s[j - 1][1] == tmp[1]:
        s[j] = s[j - 1]
        j -= 1
    s[j] = tmp

ans = []

for i in s:
    if i in ans:
        continue
    ans.append(i)
    print(ans[-1][0])
    
########## 두 번째 방법(소요 시간 약 6,000ms) ##########

import sys
input = sys.stdin.readline
n = int(input())
s = set()
for i in range(n):
    s.add(input().rstrip())
s = list(s)
ans = [None] * len(s)

for i in s:
    idx = 0
    for j in s:
        if len(i) < len(j):
            continue
        elif len(i) > len(j):
            idx += 1
        else:
            if i > j:
                idx += 1
    ans[idx] = i

print(*ans, sep="\n")

########## 세 번째 방법(소요 시간 약 2,000ms) ##########

import sys
input = sys.stdin.readline
n = int(input())
s = [input().rstrip()]
for i in range(n - 1):
    add = input().rstrip()
    idx = 0
    while True:
        if len(s[idx]) > len(add):    # 길이가 더 작을 때
            s.insert(idx, add)    # 비교한 값보다 길이 작기 때문에 그 idx에 삽입
            break
        elif len(s[idx]) == len(add):    # 길이가 같을 때
            if s[idx] > add:    # 서로 비교했을 때 사전순으로 작다면
                s.insert(idx, add)    # 삽입
                break
            elif s[idx] == add:    # 같다면 취소
                break
        else:    # 그냥 크면
            pass
        if idx == len(s) - 1:    # 마지막 인덱스까지 왔다면
            s.append(add)
            break
        idx += 1
print(*s, sep="\n")

########## 우수 풀이 ##########

import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))

"""
sort() 함수에 key를 사용한다면, 기준에 따라 정렬이 가능!!!!!!!!
새로 배운 내용이니까 잘 써먹어야겠다
"""
