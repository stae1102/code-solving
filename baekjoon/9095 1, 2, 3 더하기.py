from sys import stdin
input = stdin.readline

T = int(input())


def solve(k):
    global ans
    if k <= 0:
        if k == 0:
            ans += 1
        return

    solve(k - 1)
    solve(k - 2)
    solve(k - 3)


for _ in range(T):
    ans = 0
    solve(int(input()))
    print(ans)
