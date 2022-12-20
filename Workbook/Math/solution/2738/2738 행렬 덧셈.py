import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(*[a + b for a, b in zip(matrix_a[i], matrix_b[i])])
