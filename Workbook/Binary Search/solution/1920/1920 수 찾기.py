import sys; input = sys.stdin.readline

def binary_search(arr, k):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return 1
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return 0

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

for i in range(m):
    print(binary_search(a, num[i]))