import sys
input = sys.stdin.readline

t = int(input())


def solve():
    cnt = 0
    for choose in chooses:
        for c in range(choose[0], choose[1] + 1):
            if not visited[c]:
                visited[c] = True
                cnt += 1
                break

    return cnt


for _ in range(t):
    n, m = map(int, input().split())
    chooses = [list(map(int, input().split())) for _ in range(m)]
    chooses.sort(key=lambda x: (x[1], x[0]))
    visited = [False] * (n + 1)
    print(solve())
