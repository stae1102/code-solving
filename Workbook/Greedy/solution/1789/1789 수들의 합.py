s = int(input())
n = int((2 * s) ** .5)

if n * (n + 1) <= 2 * s:
    print(n)
else:
    print(n - 1)