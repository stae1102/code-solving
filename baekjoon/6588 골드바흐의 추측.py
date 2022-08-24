import sys

sieve = [True] * (999998)
sieve[:3] = [False, False, True]

for i in range(3, int(999997 ** .5) + 1, 2):
    if sieve[i]:
        for j in range(2 * i, 999998, i):
            sieve[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    l, r = 3, n - 3

    while l <= r:
        if sieve[l] and sieve[r]:
            print(f'{n} = {l} + {r}')
            break
        else:
            l += 2
            r -= 2
    else:
        print("Goldbach's conjecture is wrong.")
