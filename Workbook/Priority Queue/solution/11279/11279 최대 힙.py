<<<<<<< HEAD
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    command = int(input())
    if command == 0:
        try:
            print(-heapq.heappop(q))
        except:
            print(0)
    else:
=======
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    command = int(input())
    if command == 0:
        try:
            print(-heapq.heappop(q))
        except:
            print(0)
    else:
>>>>>>> origin/ubuntu
        heapq.heappush(q, -command)