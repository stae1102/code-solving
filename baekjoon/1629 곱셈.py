a, b, c = map(int, input().split())


def solve(n, s):
    if s == 1:
        return n % c
    else:
        if s % 2:
            return (n * ((solve(n, s // 2)) ** 2 % c)) % c
        else:
            return ((solve(n, s // 2)) ** 2 % c)


print(solve(a, b))
