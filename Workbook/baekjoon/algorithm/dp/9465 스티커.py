import sys
input = sys.stdin.readline

t = int(input())

def least(array, n):
    d = [[0 for _ in range(100001)] for _ in range(2)]
    d[0][1] = array[0][1]
    d[1][1] = array[1][1]
    for i in range(2, n + 1):
        d[0][i] = max(d[1][i - 1], d[1][i - 2]) + array[0][i]
        d[1][i] = max(d[0][i - 1], d[0][i - 2]) + array[1][i]
    return max(d[0][n], d[1][n])

for _ in range(t):
    n = int(input())
    array = [[0 for _ in range(n + 1)] for _ in range(2)]
    for i in range(2):
        array[i][1:] = list(map(int, input().split()))
    print(least(array, n))