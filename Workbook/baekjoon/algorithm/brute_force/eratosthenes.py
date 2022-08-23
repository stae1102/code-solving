array = [True] * (100001)

array[0], array[1] = False, False

for i in range(2, int(100001**0.5 + 1)):
    if array[i] == True:
        j = 2
        while i * j <= 100000:
            array[i * j] = False
            j += 1

for i in range(100, 500):
    if array[i] == True:
        print(i)