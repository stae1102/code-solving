from itertools import permutations
from sys import stdin
input = stdin.readline


def solve(d, idx, start):
    global ans
    # 팀이 모두 나누어지면
    if d == n // 2:
        diff = 0
        link = list(all_set - start)
        start = list(start)
        for i in range(n // 2 - 1):
            for j in range(i + 1, n // 2):
                diff += (team[start[i]][start[j]] +
                         team[start[j]][start[i]])
                diff -= (team[link[i]][link[j]] +
                         team[link[j]][link[i]])
        ans = min(ans, abs(diff))
        return

    if idx >= n:
        return

    for i in range(idx, n):
        start.add(i)
        solve(d + 1, i + 1, start)
        start.remove(i)


n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
all_set = {i for i in range(n)}
ans = 987654321

solve(0, 0, set())

print(ans)
