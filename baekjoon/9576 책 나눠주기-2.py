import sys
input = sys.stdin.readline

t = int(input())


def dfs(x):
    for i in range(len(std[x])):
        t = std[x][i]
        if visited[t]:
            continue
        visited[t] = True
        if (books[t] == 0 or dfs(books[t])):
            books[t] = x
            return True

    return False


for _ in range(t):
    n, m = map(int, input().split())
    books = [0] * (n + 1)
    std = [0]
    cnt = 0

    for _ in range(m):
        start, end = map(int, input().split())
        std.append([i for i in range(start, end + 1)])

    for i in range(1, m + 1):
        visited = [False] * (n + 1)
        if dfs(i):
            cnt += 1

    print(cnt)
