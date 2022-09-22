import sys
import heapq
input = sys.stdin.readline

n = int(input())

oil = sorted(list(map(int, input().split())) for _ in range(n))

# l: 마을까지의 거리, p: 현재 연료 상태
l, p = map(int, input().split())
cnt = 0

# j = 현재 성경이의 위치
i, j = 0, 0
pq = []

while (j + p < l):
    while i < n and p >= oil[i][0] - j:
        heapq.heappush(pq, (-oil[i][1], oil[i][0]))
        i += 1
        continue

    if not pq:
        cnt = -1
        break
    else:
        resource, dist = heapq.heappop(pq)
        p -= dist + resource - j
        j = dist
        cnt += 1

print(cnt)
