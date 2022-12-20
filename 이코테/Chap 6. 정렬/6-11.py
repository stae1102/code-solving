n = int(input())

array = []
for i in range(n):
    array.append(input().split())

array.sort(key=lambda x: int(x[1]))

for i in array:
    print(i[0], end=' ')