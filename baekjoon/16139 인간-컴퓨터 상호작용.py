<<<<<<< HEAD
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
=======
from sys import stdin
input = stdin.readline


def solve():
    s = input().rstrip()
    res = [[0] * 26]

    for i in range(len(s)):
        t = ord(s[i]) - 97

        list1 = res[-1].copy()
        list1[t] += 1

        res.append(list1)

    q = int(input())
    for _ in range(q):
        a, l, r = input().split()

        k = ord(a) - 97
        print(res[int(r) + 1][k] - res[int(l)][k])


if __name__ == "__main__":
    solve()
>>>>>>> 8dc1ef8861f97e403a478f8bb0d2b1d34c51b8f2
