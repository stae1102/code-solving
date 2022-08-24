import sys
input = sys.stdin.readline

m = 50000000
sieve = [True] * (m + 1)
sieve[:3] = [False, False, True]

primes = [2]

for i in range(3, m + 1, 2):
    if sieve[i]:
        primes.append(i)
        for j in range(2 * i, m + 1, i):
            sieve[j] = False

def is_prime(num):
    if num > m:
        for prime in primes:
            if num % prime == 0:
                return False
        return True

    else:
        return sieve[num]


t = int(input())

for _ in range(t):
    k = sum(map(int, input().split()))
    if k < 4:
        print("NO")
    elif k % 2 == 0:
        print("YES")
    else:
        if is_prime(k - 2):
            print("YES")
        else:
            print("NO")
