""" 
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
"""
priorities = [1, 1, 3, 2, 1, 4, 1, 1, 3, 1, 1, 1]
location = int(input())

def solution(p,l):
    front = 0
    count = 0
    m = max(p)
    while True:
        if p[l] == 0:
            return count
        if m == p[front]:
            count += 1
            p[front] = 0
            m = max(p)
        front += 1
        if front == len(p):
            front = 0

print(solution(priorities, location))
