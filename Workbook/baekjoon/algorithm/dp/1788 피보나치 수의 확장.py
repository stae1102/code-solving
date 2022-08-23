import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
mod = 1000000000

def mul(a, b):
    tmp = [[0] * 2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += (a[i][k] * b[k][j]) % mod

    return tmp


def solve(a, b):
    if b == 1:
        return a
    
    tmp = solve(a, b // 2)
    if b % 2: return mul(mul(tmp, tmp), a)
    else: return mul(tmp, tmp)

if n < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
    print(solve([[1, 1], [1, 0]], abs(n) - 1)[0][0] % mod)
elif n == 0:
    print(0)
    print(0)

else: # n > 0일 때
    print(1)
    print(solve([[1, 1], [1, 0]], n - 1)[0][0] % mod)