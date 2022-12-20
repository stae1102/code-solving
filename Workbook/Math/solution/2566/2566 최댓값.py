MAX = -1
c = [0, 0]

for i in range(9):
    num = list(map(int, input().split()))
    for j in range(9):
        if num[j] > MAX:
            MAX = num[j]
            c = [i + 1, j + 1]

print(MAX)
print(*c)
