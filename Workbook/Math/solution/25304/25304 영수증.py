import sys
input = sys.stdin.readline
all_cost = int(input())
n = int(input())

calculated_cost = 0
for i in range(n):
    cost, cnt = map(int, input().split())
    calculated_cost += cost * cnt

answer = ['No', 'Yes']
print(answer[calculated_cost == all_cost])
