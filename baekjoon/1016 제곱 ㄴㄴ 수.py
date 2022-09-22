x, y = map(int, input().split())


def solve(x, y):
    ans = y - x + 1
    sieve = [False] * (y - x + 1)
    i = 2

    while i ** 2 <= y:
        sqrt = i ** 2
        mod = 0 if x % sqrt == 0 else 1
        nearest = x // sqrt + mod
        while sqrt * nearest <= y:
            if not sieve[sqrt * nearest - x]:
                sieve[sqrt * nearest - x] = True
                ans -= 1
            nearest += 1
        i += 1

    return ans


print(solve(x, y))
