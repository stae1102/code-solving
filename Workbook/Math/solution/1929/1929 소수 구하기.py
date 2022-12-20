def prime_list(a, b):
    sieve = [True] * (b + 1)
    sieve[0], sieve[1] = False, False

    m = int(n ** .5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i * 2, b + 1, i):
                sieve[j] = False

    return [i for i in range(a, b + 1) if sieve[i] == True]


m, n = map(int, input().split())

print(*prime_list(m, n))
