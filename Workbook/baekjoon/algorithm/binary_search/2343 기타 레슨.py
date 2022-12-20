n, m = map(int, input().split())
array = list(map(int, input().split()))

left = max(array)
right = sum(array)
result = 987654321

while left <= right:
    mid = (left + right) // 2
    cnt, temp = 1, 0
    for i in array:
        if temp + i > mid:
            temp = 0
            cnt += 1
        temp += i
    if cnt <= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1
    
print(result)