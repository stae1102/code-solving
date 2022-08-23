n = int(input())
s = sorted(map(int, input().split()))

if n % 2 == 0:
    print(s[0] * s[-1])
else:
    print(s[n // 2] ** 2)
