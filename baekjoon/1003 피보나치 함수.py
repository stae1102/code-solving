import sys
input = sys.stdin.readline

T = int(input())

fibo = [[0, 0] for _ in range(41)]

fibo[0] = [1, 0]
fibo[1] = [0, 1]

for i in range(2, 41):
    fibo[i] = [fibo[i - 1][0] + fibo[i - 2]
               [0], fibo[i - 1][1] + fibo[i - 2][1]]

for _ in range(T):
    k = int(input())
    print(*fibo[k])
