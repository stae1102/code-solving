import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        try:
            print(heapq.heappop(arr)[1])
        except:
            print(0)
    else:
        heapq.heappush(arr, (abs(tmp), tmp))
