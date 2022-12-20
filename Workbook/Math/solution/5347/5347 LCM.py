import sys
input = sys.stdin.readline


def gcd(n, m):
    tmp = n % m
    while tmp != 0:
        n = m
        m = tmp
        tmp = n % m

    return m


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
