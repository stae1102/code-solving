def eratosthenes(k):
    sieve = [True] * (k + 1)
    sieve[:2] = [False, False]
    prime_numbers = []

    for i in range(2, int(k ** .5) + 1):
        if sieve[i]:
            for j in range(i * 2, k + 1, i):
                sieve[j] = False

    for i in range(2, k + 1):
        if sieve[i]:
            prime_numbers.append(i)

    return prime_numbers


n = int(input())

prime_numbers = eratosthenes(n)

l = len(prime_numbers)
result = 0
summary = 0
end = 0

for start in range(l):
    while summary < n and end < l:
        summary += prime_numbers[end]
        end += 1

    if summary == n:
        result += 1

    summary -= prime_numbers[start]

print(result)
