from collections import deque
import sys
input = sys.stdin.readline

'''
1. for 반복문으로 1~N까지의 컴퓨터를 BFS로 순회
2. visited[i]가 True일 경우 무시
3. visited[i]가 False일 경우 cnt + 1하며 카운팅하기
'''

N = int(input())
M = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    cnt = 0
    visited[v] = True
    q = deque([v])

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)

    return cnt

print(bfs(1))
