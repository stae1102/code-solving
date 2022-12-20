from sys import stdin


def eratosthenes(n):
    prime_numbers = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if prime_numbers[i]:
            for k in range(i * 2, n + 1, i):
                prime_numbers[k] = False

    return prime_numbers


n = int(stdin.readline())

l = eratosthenes(1001)
ans = 0

k = list(map(int, stdin.readline().split()))

for i in k:
    if l[i]:
        ans += 1

print(ans)
