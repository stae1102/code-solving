l = [int(input()) for _ in range(3)]
m = list(map(int, str(l[0] * l[1] * l[2])))
for i in range(10):
    print(m.count(i))
