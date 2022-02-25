import sys
input = sys.stdin.readline
a = input()
b = list(map(int, input().split()))
b.sort()
ans = 0
for i in range(len(b)):
    ans += sum(b[:i + 1])
print(ans)
