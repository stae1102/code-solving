import sys
input = sys.stdin.readline

def solve(arr):
    d = [[0, 0, 0] for _ in range(n)]
    d[0] = arr[0]
    d[0][2] += d[0][1]
    d[1][0] = d[0][1] + arr[1][0]; d[1][1] = min(d[0][1], d[0][2], d[1][0]) + arr[1][1]
    d[1][2] = min(d[0][1], d[0][2], d[1][1]) + arr[1][2]
    for i in range(2, n):
        d[i][0] = min(d[i - 1][0], d[i - 1][1]) + arr[i][0]
        d[i][1] = min(d[i - 1]) + arr[i][1]
        d[i][2] = min(d[i - 1][1], d[i - 1][2]) + arr[i][2]
        d[i][1] = min(d[i][1], d[i][0] + arr[i][1])
        d[i][2] = min(d[i][2], d[i][1] + arr[i][2])

    return d[n - 1][1]

i = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = solve(graph)
    print(f'{i}. {ans}')
    i += 1