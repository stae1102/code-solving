import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(x):
    for i in range(len(cows[x])):
        t = cows[x][i]
        if visited[t]:
            continue
        visited[t] = True
        if (houses[t] == 0 or dfs(houses[t])):
            houses[t] = x
            return True
    return False


cows = [0] + [list(map(int, input().split()))[1:] for _ in range(n)]
houses = [0] * (m + 1)
cnt = 0

for i in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(i):
        cnt += 1

print(cnt)
