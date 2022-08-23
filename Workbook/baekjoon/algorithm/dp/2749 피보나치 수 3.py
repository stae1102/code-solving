import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())

def mul(a, b):
    TMP = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                TMP[i][j] += (a[i][k] * b[k][j]) % 1000000

    return TMP

def solve(a, b):
    if b == 1:
        return a

    tmp = solve(a, b // 2)
    if b % 2: return mul(mul(tmp, tmp), a)
    else: return mul(tmp, tmp)

ans = solve([[1, 1], [1, 0]], n - 1)[0][0] % 1000000
print(ans)