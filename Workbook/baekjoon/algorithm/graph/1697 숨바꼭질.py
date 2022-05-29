from collections import deque

n, k = map(int, input().split())
m = 100001    # 최대 가능 범위
visited = [False] * m    # 방문 기록 설정

def bfs(v):
    q = deque([[v, 0]])    # 현 위치와 걸린 일 수
    while q:
        v, x = q.popleft()
        if not visited[v]:    # 방문하지 않았을 때
            visited[v] = True
            if v == k:    # 도착했으면
                return x
            x += 1    # 1일 추가
            if v - 1 >= 0:
                q.append([v - 1, x])
            if v + 1 <= 100000:
                q.append([v + 1, x])
            if 2 * v <= 100000:
                q.append([2 * v, x])

print(bfs(n))
