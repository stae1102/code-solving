import heapq
import sys
input = sys.stdin.readline

n = int(input())

leftheap = []
rightheap = []
answer = []

for _ in range(n):
    m = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-m, m))
    else:
        heapq.heappush(rightheap, (m, m))

    if rightheap and leftheap[0][1] > rightheap[0][0]:
        MAX = heapq.heappop(leftheap)[1]
        MIN = heapq.heappop(rightheap)[0]
        heapq.heappush(leftheap, (-MIN, MIN))
        heapq.heappush(rightheap, (MAX, MAX))

    answer.append(leftheap[0][1])

for i in answer:
    print(i)