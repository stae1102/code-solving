from sys import stdin
input = stdin.readline


def solve(k, start, end):
    ans = 0
    for i in range(start, end + 1):
        if s[i] == k:
            ans += 1

    return ans


s = input().rstrip()

q = int(input())

for _ in range(q):
    k, start, end = input().split()
    cnt = solve(k, int(start), int(end))
    print(cnt)
