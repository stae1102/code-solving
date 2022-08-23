array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search(array, 7, 0, len(array) - 1)
print(result)