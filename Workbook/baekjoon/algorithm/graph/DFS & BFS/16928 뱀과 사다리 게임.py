from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dice = [i for i in range(1, 7)]

radder = [0 for _ in range(101)]
snake = [0 for _ in range(101)]
visited = [False] * 101
visited_snake = [False] * 101

for _ in range(n):
    start, end = map(int, input().split())
    radder[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    snake[start] = end


def bfs(v):
    q = deque([[v, 0]])
    while q:
        v, x = q.popleft()
        if v == 100:
            return x
        x += 1
        for i in dice:
            nv = v + i
            if nv > 100 or visited[nv] or visited_snake[nv]:
                continue
            visited[nv] = True
            if radder[nv] != 0:
                q.append([radder[nv], x])
            elif snake[nv] != 0:
                q.append([snake[nv], x])
                visited_snake[nv] = True
            else:
                q.append([nv, x])

print(bfs(1))