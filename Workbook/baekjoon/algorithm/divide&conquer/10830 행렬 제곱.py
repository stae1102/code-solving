import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul(X, Y):
    TMP = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += X[i][k] * Y[k][j]
            TMP[i][j] = tmp % 1000
    
    return TMP

def solve(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    
    tmp = solve(A, B // 2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

ans = solve(A, B)
for i in ans:
    print(*i)