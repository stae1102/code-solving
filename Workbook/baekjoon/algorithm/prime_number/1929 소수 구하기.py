import math

array = [True] * (1000001)

array[0], array[1] = False, False

for i in range(2, int(math.sqrt(1000001) + 1)):
    if array[i] == True:
        j = 2
        while i * j < 1000001:
            array[i * j] = False
            j += 1
n, m = map(int, input().split())

for i in range(n, m + 1):
    if array[i] == True:
        print(i)