d = [[0 for _ in range(5)] for _ in range(2)]

for i in range(2):
    d[i][1:] = list(map(int, input().split()))
    print(d[i][1:])
    print(d)