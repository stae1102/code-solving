import sys
m, n = map(int, sys.stdin.readline().split())
scale = 1000000
a = [False, False] + [True] * (scale - 1)
primes = set()
for i in range(2, scale + 1):
    if a[i]:
        primes.add(i)
        for j in range(2 * i, scale + 1, i):
            a[j] = False
for i in range(m, n + 1):
    if i in primes:
        sys.stdout.write(str(i) + "\n")
        
"""
1. set을 사용하는 방법이 복잡도가 확실히 줄어드는 방법.
2. 원소들을 for문으로 돌리며 판별
"""
