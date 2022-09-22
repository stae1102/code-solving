import sys
input = sys.stdin.readline

t = int(input())


def dfs(a):
    if visited[a]:
        return False
    visited[a] = True
    for b in V[a]:
        if (B[b] == 0 or (not visited[B[b]] and dfs(B[b]))):
            A[a] = b
            B[b] = a
            return True

    return False


for _ in range(t):
    n, m = map(int, input().split())
    # a: 학생, b: 책
    # v: 간선
    A, B = [0] * (m + 1), [0] * (n + 1)
    V = [[]]
    cnt = 0

    for _ in range(m):
        start, end = map(int, input().split())
        V.append([i for i in range(start, end + 1)])

    for i in range(1, m + 1):
        if A[i] == 0:
            visited = [False] * (m + 1)
            if dfs(i):
                cnt += 1

    print(cnt)
