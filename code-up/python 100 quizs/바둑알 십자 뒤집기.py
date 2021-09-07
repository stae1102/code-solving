d = []
for i in range(19):
    d.append(list(map(int, input().split())))

n = int(input())
# x 값 뒤집기 - y만 바뀌면 됨
for k in range(n):
    x, y = list(map(int, input().split()))
    for i in range(19):
        if d[x - 1][i] == 0:
            d[x - 1][i] = 1
        else:
            d[x - 1][i] = 0
            
        if d[i][y - 1] == 0:
            d[i][y - 1] = 1
        else:
            d[i][y - 1] = 0

for i in range(19):
    for j in range(19):
        print(str(d[i][j]), end=' ')
    print()
