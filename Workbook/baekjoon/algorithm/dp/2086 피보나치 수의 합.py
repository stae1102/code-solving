import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
mod = 1000000000
a, b = map(int, input().split())

def mul(a, b):
    TMP = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                TMP[i][j] += (a[i][k] * b[k][j]) % mod

    return TMP

def solve(a, b):
    if b == 1:
        return a

    tmp = solve(a, b // 2)
    if b % 2: return mul(mul(tmp, tmp), a)
    else: return mul(tmp, tmp)

ans = 0
# ans = solve([[1, 1], [1, 0]], n - 1)[0][0] % 1000000
for i in range(a, b + 1):
    ans += solve([[1, 1], [1, 0]], i - 1)[0][0] % mod
print(ans % mod)