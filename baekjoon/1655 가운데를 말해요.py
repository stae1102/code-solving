import sys
import heapq
input = sys.stdin.readline

n = int(input())

left, right = [], []

for _ in range(n):
    k = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-k, k))  # 좌측은 최대 힙이 필요
    else:
        heapq.heappush(right, (k, k))  # 우측은 최소 힙이 필요, 간단한 출력을 위해 입력 양식 통일

    if right and left[0][1] > right[0][1]:
        MIN = heapq.heappop(right)[1]
        MAX = heapq.heappop(left)[1]
        heapq.heappush(left, (-MIN, MIN))
        heapq.heappush(right, (MAX, MAX))

    print(left[0][1])
