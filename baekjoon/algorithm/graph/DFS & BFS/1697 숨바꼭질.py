from collections import deque
N, K = map(int, input().split())

q = deque([(N, 0)])
visited = [0] * 100001

def bfs():
    while q:
        N, cnt = q.popleft()
        for i in [N-1, N+1, 2*N]:
            if 0 <= i < 100001 and not visited[i]:
                if i == K:
                    return cnt + 1
                q.append((i, cnt + 1))

print(bfs())