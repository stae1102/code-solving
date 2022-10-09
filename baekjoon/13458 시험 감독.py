n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = n


def solve(k):
    num = k - b
    if num <= 0:
        return 0
    else:
        count = num // c
        mod = 1 if num % c else 0
        return count + mod


ans += sum(list(map(solve, a)))

print(ans)
