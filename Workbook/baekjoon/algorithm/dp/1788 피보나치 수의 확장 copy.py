import sys
input = sys.stdin.readline
n = int(input())
mod = 1000000000

def fibo(n):
    size = 2
    
    def square_matrix_mul(a, b, size=size):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += (a[i][k] * b[k][j]) % mod
                    new[i][j] %= mod

        return new

    def get_nth(n):
        k = 0
        zero = [[1, 0], [0, 1]]
        base = [[1, 1], [1, 0]]

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                zero = square_matrix_mul(zero, base)
            k += 1
            base = square_matrix_mul(base, base)

        return zero
    
    return get_nth(n)[1][0]
            
val = fibo(abs(n))

if n > 0:
    print(1)
elif n == 0:
    print(0)
else:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
print(val)