import sys
import heapq
input = sys.stdin.readline

# 포커스는 보석의 무게
# 보석의 무게를 우선순위 큐로 뽑아내면서 무게를 찾아나서면 됨.
n, k = map(int, input().split())

gems = sorted(list(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))
q = []
ans = 0
j = 0

for i in range(k):
    while (j < n) and (gems[j][0] <= bags[i]):
        heapq.heappush(q, -gems[j][1])
        j += 1

    if q:
        ans -= heapq.heappop(q)

print(ans)
