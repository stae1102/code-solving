def rotate(arr):
    return list(zip(*arr[::-1]))

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
