import sys; input = sys.stdin.readline

def binary_search(arr, x):
    start = 1
    end = max(arr)
    
    while start <= end:
        mid = (start + end) // 2
        average = 0

        for i in arr:
            average += i // mid

        if average < x:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

print(binary_search(lan, n))