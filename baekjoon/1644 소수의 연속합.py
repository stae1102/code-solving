def eratosthenes(k):
    if k < 2:
        return []
    sieve = [True] * (k + 1)
    sieve[:2] = [False, False]
    prime_numbers = [2]

    for i in range(3, int(k ** .5) + 2, 2):
        if sieve[i]:
            for j in range(i * 2, k + 1, i):
                sieve[j] = False
    print(sieve)

    for i in range(3, k + 1, 2):
        if sieve[i]:
            prime_numbers.append(i)

    return prime_numbers


n = int(input())

prime_numbers = eratosthenes(n)
print(prime_numbers)
# l = len(prime_numbers)
# result = 0
# summary = 0
# end = 0

# for start in range(l):
#     while summary < n and end < l:
#         summary += prime_numbers[end]
#         end += 1

#     if summary == n:
#         result += 1

#     summary -= prime_numbers[start]

# print(result)
