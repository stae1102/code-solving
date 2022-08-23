n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

ans = []

def solve(cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(arr[i])
        solve(cnt + 1)
        ans.pop()

solve(0)