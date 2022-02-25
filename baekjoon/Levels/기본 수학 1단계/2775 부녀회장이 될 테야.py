import sys

def apart(f: int, n: int) -> int:
    """각 층과 호 수로 재귀함수"""
    if f == 0:
        return n
    elif n == 1:
        return 1
    else:
        return apart(f - 1, n) + apart(f, n - 1)

n = int(sys.stdin.readline())
for i in range(n):
    floor = int(sys.stdin.readline())
    number = int(sys.stdin.readline())
    print(apart(floor, number))

################# 우수 사례 ###################
    
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])
