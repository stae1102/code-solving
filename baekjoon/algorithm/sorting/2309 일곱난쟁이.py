import sys
array = [int(sys.stdin.readline()) for _ in range(9)]
array.sort()
h = sum(array)

def find(array):
    for i in range(8):
        for j in range(i + 1, 9):
            if h - (array[i] + array[j]) == 100:
                array[i] = array[j] = 0
                return

find(array)

for i in array:
    if i:
        print(i, end="\n")
