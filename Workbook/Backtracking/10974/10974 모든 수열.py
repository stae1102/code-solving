n = int(input())
num = [i for i in range(1, n + 1)]

visited = [False] * n
arr = []

def solve(cnt):
    if cnt == n:
        print(*arr)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(num[i])
            solve(cnt + 1)
            visited[i] = False
            arr.pop()

solve(0)