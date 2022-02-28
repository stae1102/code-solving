import sys
input = sys.stdin.readline
n = int(input())
array_n = list(map(int, input().rstrip().split()))
array_n.sort()

m = int(input())
array_m = list(map(int, input().rstrip().split()))
array_m.sort()

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

for i in array_m:
    if binary_search(array_n, i, 0, len(array_n) - 1) != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')