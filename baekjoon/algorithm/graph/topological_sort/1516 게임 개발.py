import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
cost = [0] * (n + 1)    # 걸린 시간
indegree = [0] * (n + 1)    # 진입차수
graph = [[] for _ in range(n + 1)]    # 각 노드에 담긴 간선 정보

# 간선 정보 입력받기
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]         # 입력의 첫 번째 수는 비용
    for j in temp[1:-1]:      # 그 이후 -1까지는 방향
        indegree[i] += 1      # 진입차수 추가
        graph[j].append(i)    # 노드에 연결된 간선

def topology_sort():          # 위상 정렬 함수정의
    q = deque()
    result = cost[:]          # 결과값 리스트

    for i in range(1, n + 1):
        if indegree[i] == 0:  # 진입차수가 0인 노드 먼저
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + cost[i])    # 걸린 시간의 최댓값 구하기
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

topology_sort()
