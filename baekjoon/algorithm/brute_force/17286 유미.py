import math
import heapq

x, y = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
visited = [True, False, False, False]

ans = 0

def cal(a, b):
    return math.sqrt((a ** 2 + b ** 2))

while len(array):
    q = []
    for i in range(len(array)):
        if not visited[i]:
            heapq.heappush(q, (cal(x - array[i][0], y - array[i][1]), i))
    if q:
        min_len, min_idx = heapq.heappop(q)
        x, y = array[min_idx][0], array[min_idx][1]
        visited[min_idx] = True
        del array[min_idx]
    print(array)
    ans += min_len

print(ans)