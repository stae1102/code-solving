w = input()

arr = []
n = len(w)
for i in range(0, n - 2):
    for j in range(i+1, n - 1):
        first = w[:i+1]
        second = w[i+1:j+1]
        third = w[j+1:]
        arr.append(first[::-1]+second[::-1]+third[::-1])

arr = sorted(arr)[0]
print(arr)