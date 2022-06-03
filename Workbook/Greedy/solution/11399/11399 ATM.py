N = int(input())
P = list(map(int, input().split()))
P.sort()

ans = 0

for (i, j) in zip(P, range(N, 0, -1)):
    ans += i * j

print(ans)