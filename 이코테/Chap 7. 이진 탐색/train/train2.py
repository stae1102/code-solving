array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = 13

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

idx = binary_search(array, target, 0, len(array) - 1)
print(idx)