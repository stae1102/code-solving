from collections import deque
import sys
import copy
input = sys.stdin.readline

# 처음에는 엣지 값에 빈 값을 넣어서 초기화 하도록 함


def melt_cheese():
    cnt = 0
    while edges:
        x, y = edges.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    next_edges.append((nx, ny))
                    continue
                edges.append((nx, ny))

    return cnt


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
day = 0

r, c = map(int, input().split())
graph = []
for _ in range(r):
    row = list(map(int, input().split()))
    cnt += sum(row)
    graph.append(row)
next_graph = copy.deepcopy(graph)

visited = [[False] * c for _ in range(r)]

edges = deque([(0, 0)])
next_edges = deque()

while cnt != 0:
    cnt -= melt_cheese()
    day += 1
    edges, next_edges = next_edges, edges

print(day)
print(len(edges) if day else 0)
