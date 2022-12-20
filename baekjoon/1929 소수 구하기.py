from sys import stdin


def eratosthenes(n):
    prime_numbers = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** .5) + 1):
        if prime_numbers[i]:
            for k in range(i * 2, n + 1, i):
                prime_numbers[k] = False

    return prime_numbers


start, end = map(int, stdin.readline().split())

l = eratosthenes(end)

for i in range(start, end + 1):
    if l[i]:
        print(i)
