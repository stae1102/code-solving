import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {}
ans = 0

for _ in range(n):
    word = input().rstrip()
    s[word] = 1

for _ in range(m):
    word = input().rstrip()
    if word in s:
        ans += 1

print(ans)