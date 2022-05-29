# n = int(input())
# d = [0] * 100001
# d[1] = 3
# d[2] = 7

# for i in range(3, n + 1):
#     d[i] = (d[i - 2] + d[i - 1] * 2) % 9901

# print(d[n])

n = int(input())
d = [[0, 0, 0] for _ in range(n + 1)]
d[1] = [1, 1, 1]

for i in range(2, n + 1):
    d[i][0] = (d[i - 1][0] + d[i - 1][1] + d[i - 1][2]) % 9901
    d[i][1] = (d[i - 1][0] + d[i - 1][2]) % 9901
    d[i][2] = (d[i - 1][0] + d[i - 1][1]) % 9901

print(sum(d[n]) % 9901)