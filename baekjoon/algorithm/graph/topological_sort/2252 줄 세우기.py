from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)              # 진입차수
graph = [[] for _ in range(n + 1)]    # 노드 관계

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1    # 진입차수 추가

def topology_sort():
    result = []    # 결과를 출력할 리스트
    q = deque()    # 큐 사용

    for i in range(1, n + 1):
        if indegree[i] == 0:    # 처음 시작하는 노드들
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=" ")

topology_sort()
