def counting_sort(arr):
    counting = [0] * (max(arr) + 1)
    
    l = []

    for i in range(len(arr)):
        counting[arr[i]] += 1
    
    for x in range(len(counting)):
        for _ in range(counting[x]):
            l.append(x)
    return l
            

n = int(input())
a = counting_sort(list(map(int, input().split())))
b = reversed(counting_sort(list(map(int, input().split()))))

ans = 0

for (x, y) in zip(a, b):
    ans += x * y

print(ans)