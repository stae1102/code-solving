import sys
r = sys.stdin.readline

t = int(r())

def solve(n):
    s = [0] * (n + 1)
    for _ in range(n):
        x, y = map(int, r().split())
        s[x] = y

    MIN = n
    for i in range(1, n + 1):
        if MIN < s[i]:
            n -= 1
        else:
            MIN = min(MIN, s[i])
    return n

for _ in range(t):
    print(solve(int(r())))