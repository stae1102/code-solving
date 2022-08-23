# 깊이 우선 탐색은 DFS고 너비 우선 탐색은 BFS인데 또 헷갈렸다 ㅠㅠ
# 어차피 문제 보고 재귀인 줄 알았으므로, 다음부터는 문제 유형을 잘 체크하자
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

def bfs():
    q = deque()
    q.append((x, ''))

    while q:
        num, ans = q.popleft()
        D = (num * 2) % 10000
        if D == target: return ans + 'D'
        elif not visited[D]:
            visited[D] = 1
            q.append((D, ans + 'D'))

        S = num - 1 if num > 0 else 9999
        if S == target: return ans + 'S'
        elif not visited[S]:
            visited[S] = 1
            q.append((S, ans + 'S'))

        L = int(num % 1000 * 10 + num / 1000)
        if L == target: return ans + 'L'
        elif not visited[L]:
            visited[L] = 1
            q.append((L, ans + 'L'))

        R = int(num % 10 * 1000 + num // 10)
        if R == target: return ans + 'R'
        elif not visited[R]:
            visited[R] = 1
            q.append((R, ans + 'R'))

for _ in range(T):
    x, target = map(int, input().split())
    visited = [0 for _ in range(10001)]
    print(bfs())