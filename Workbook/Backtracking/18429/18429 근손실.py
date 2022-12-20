<<<<<<< HEAD
n, k = map(int, input().split())
w = list(map(int, input().split()))

ans = 0
visited = [False] * n

def solve(kg, cnt):
    global ans

    # 백트래킹 중 500이하로 감소하면 바로 되돌아감
    if kg < 500:
        return

    # 정상적으로 루틴을 작성했을 때
    if cnt == n:
        ans += 1

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solve(kg - k + w[i], cnt + 1)
            visited[i] = False

solve(500, 0)

=======
n, k = map(int, input().split())
w = list(map(int, input().split()))

ans = 0
visited = [False] * n

def solve(kg, cnt):
    global ans

    # 백트래킹 중 500이하로 감소하면 바로 되돌아감
    if kg < 500:
        return

    # 정상적으로 루틴을 작성했을 때
    if cnt == n:
        ans += 1

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            solve(kg - k + w[i], cnt + 1)
            visited[i] = False

solve(500, 0)

>>>>>>> origin/ubuntu
print(ans)