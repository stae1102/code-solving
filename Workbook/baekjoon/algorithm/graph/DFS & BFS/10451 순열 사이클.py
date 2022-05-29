from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs(arr, visited, start):
    if visited[start]:
        return 0
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        if not visited[arr[now]]:
            visited[arr[now]] = True
            q.append(arr[now])
    return 1

for _ in range(t):
    n = int(input())
    arr = [0] * (n + 1)
    arr[1:] = list(map(int, input().split()))
    visited = [False] * (n + 1)
    cycles = 0

    for i in range(1, n + 1):
        cycles += bfs(arr, visited, i)
    
    print(cycles)