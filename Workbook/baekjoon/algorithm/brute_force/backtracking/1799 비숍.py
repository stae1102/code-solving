import sys
input = sys.stdin.readline

N = int(input())

chess = [list(map(int, input().split())) for _ in range(N)]
d = [0] * (2 * N - 1)

def fn(n):
    if n > 2 * N - 1:
        return 0
    
    ans = -1
    x, y = (0, n) if n < N else (n - (N - 1), N - 1)
    while y >= 0 and x < N:
        if (chess[y][x] == 1 and d[x - y + N - 1] == 0):
            d[x - y + N - 1] = 1
            temp = fn(n + 2) + 1
            ans = max(ans, temp)
            d[x - y + N - 1] = 0

        x += 1
        y -= 1
    
    if ans < 0:
        ans = max(ans, fn(n + 2))

    return ans

fn_0 = fn(0)
fn_1 = fn(1)

print(fn_0 + fn_1)