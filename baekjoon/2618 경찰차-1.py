import sys
input = sys.stdin.readline
n = int(input())
w = int(input())


def calc(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def get_distance(a, b):
    if a == n or b == n:
        return 0

    if dist[a][b] != -1:
        return dist[a][b]

    next = max(a, b) + 1

    distA = calc(path_A[next], path_A[a])
    distB = calc(path_B[next], path_B[b])

    goA = get_distance(next, b) + distA
    goB = get_distance(a, next) + distB

    dist[a][b] = min(goA, goB)
    return dist[a][b]


dist = [[-1] * (w + 1) for _ in range(w + 1)]
path_A = [[1, 1]]
path_B = [[n, n]]

for _ in range(w):
    x, y = map(int, input().split())
    path_A.append([x, y])
    path_B.append([x, y])
