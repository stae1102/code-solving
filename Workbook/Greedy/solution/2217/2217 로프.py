import sys
input = sys.stdin.readline

N = int(input())

rope = [int(input()) for _ in range(N)]

'''
You should sort and flip the list.
Because even if there are many ropes, the point is the least weight.
The key is that largest weight can be multiplied by (least weight * index).
'''

rope.sort(reverse = True)
ans = -1

for i in range(N):
    temp = rope[i] * (i + 1)
    if ans < temp:
        ans = temp

print(ans)