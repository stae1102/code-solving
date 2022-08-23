import math
import sys
input = sys.stdin.readline

N = int(input())

def solve(arr):
    m, n, x, y = arr
    while x <= math.lcm(m, n):
        if x % n == y % n:
            return x
        x += m
    return -1

for _ in range(N):
    data = list(map(int, input().split()))
    print(solve(data))