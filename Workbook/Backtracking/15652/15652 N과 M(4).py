<<<<<<< HEAD
n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

ans = []

def solve(idx, cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(idx, n):
        ans.append(arr[i])
        solve(i, cnt + 1)
        ans.pop()

=======
n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

ans = []

def solve(idx, cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(idx, n):
        ans.append(arr[i])
        solve(i, cnt + 1)
        ans.pop()

>>>>>>> origin/ubuntu
solve(0, 0)