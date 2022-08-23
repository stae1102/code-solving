import math

n = int(input())

numbers = [True] * (n + 1)
numbers[:2] = [False, False]
for i in range(2, int(math.sqrt(n) + 1)):
    if numbers[i] == True:
        j = 2
        while i * j <= n:
            numbers[i * j] = False
            j += 1

for i in range(len(numbers)):
    if numbers[i]:
        print(i, end=' ')