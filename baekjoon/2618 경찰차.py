import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
w = int(input())


def get_distance(a, b):
    if a == w or b == w:
        return 0

    if dist[a][b] != -1:
        return dist[a][b]

    latest = max(a, b) + 1

    distA = calc(path_A[latest], path_A[a])
    distB = calc(path_B[latest], path_B[b])

    go_A = get_distance(latest, b) + distA
    go_B = get_distance(a, latest) + distB

    dist[a][b] = min(go_A, go_B)
    return dist[a][b]


def find_path(a, b):
    if a == w or b == w:
        return

    latest = max(a, b) + 1

    distA = calc(path_A[latest], path_A[a])
    distB = calc(path_B[latest], path_B[b])

    go_A = get_distance(latest, b) + distA
    go_B = get_distance(a, latest) + distB

    if go_A > go_B:
        print(2)
        find_path(a, latest)
    else:
        print(1)
        find_path(latest, b)


def calc(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


dist = [[-1] * (w + 1) for _ in range(w + 1)]
path_A = [[1, 1]]
path_B = [[n, n]]

for _ in range(w):
    x, y = map(int, input().split())
    path_A.append([x, y])
    path_B.append([x, y])

print(get_distance(0, 0))
find_path(0, 0)
