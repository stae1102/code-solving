import sys
import heapq

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readlines()))
ans = 0

heapq.heapify(cards)

while len(cards) != 1:
    result = heapq.heappop(cards) + heapq.heappop(cards)
    ans += result
    heapq.heappush(cards, result)

print(ans)
