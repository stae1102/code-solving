import sys
scale = 246912
a = [False, False] + [True] * (scale - 1)
primes = set()
for i in range(2, scale + 1):
    if a[i]:
        primes.add(i)
        for j in range(2 * i, scale + 1, i):
            a[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, n * 2 + 1):
        if i in primes:
            count += 1
    print(count)
