import sys
n = int(sys.stdin.readline())
for _ in range(n):
    k, d = map(int, sys.stdin.readline().split())
    ans = 0
    for _ in range(k):
        v, f, c = map(int, sys.stdin.readline().split())
        if v * f // c >= d:
            ans += 1
    print(ans)
