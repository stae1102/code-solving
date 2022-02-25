import sys
import math
input = sys.stdin.readline
n, m = int(input()), int(input())
graph = [[math.inf] * (n + 1) for _ in range(n + 1)]    # 그래프를 무한대로 초기화

# 자기 자신으로 가는 거리는 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 노드를 이어주는 간선을 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == math.inf or graph[a][b] > c:    # 중복된 간선에서 최소한의 거리를 구하기 위해 가중치가 높으면 제외
        graph[a][b] = c

# 노드 탐색
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])    # 바로 가는 것이 빠른지 다른 노드를 거쳐 가는 것이 빠른지 탐색

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == math.inf:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
