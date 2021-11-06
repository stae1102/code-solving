import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]    # 그래프 생성
visited = [False] * n             # 방문기록 저장

#######################
##### 그래프 생성 #####
#######################

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = False

def dfs(v, cnt):
    global ans
    if cnt >= 4:
        ans = True
        return
    for i in graph[v]:
        if not visited[i]:
            visited[v] = True
            dfs(i, cnt + 1)
            visited[v] = False    # 깊이 들어가지 못했기 때문에 그 노드는 비방문처리로 재사용할 수 있도록 한다

for i in range(n):
    visited = [False] * n
    dfs(i, 0)
    if ans:
        print(1)
        exit()
else:
    print(0)
