def binary_search(arr, n):
    pl = 0
    pr = len(arr) - 1
    num = 0
    while pl <= pr:
        mid = (pl + pr) // 2
        if arr[mid] >= n:
            num = mid
            pr = mid - 1
        else:
            pl = mid + 1
    return True if arr[num] == n else False

n = int(input())
card = sorted(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))

for i in range(m):
    if binary_search(card, compare[i]):
        print(1, end=' ')
    else:
        print(0, end=' ')