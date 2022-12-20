n, m = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)
print(arr[m - 1])
