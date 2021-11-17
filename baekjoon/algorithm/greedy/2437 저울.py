import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()    # 가장 작은 단위부터 늘려가기 시작

target = 1    # 가장 적은 값

"""
1. target 값에 계속 값을 오름차순으로 더해간다. target 미만 값은 계속 우리가 만들 수 있는 값임.
ex) target = 1이고, x = 1 -> target += x, target = 2.
    target = 2이고, x = 2 -> target = 4 (3 이하 값은 모두 만들 수 있다.)
    target = 4이고, x = 3 -> target = 7 (6 이하 값은 다 만들 수 있다.)
2. target 보다 작은 값이 나오면 그 값은 만들 수 없다.
"""

for x in data:
    if target < x:
        break
    target += x

print(target)
