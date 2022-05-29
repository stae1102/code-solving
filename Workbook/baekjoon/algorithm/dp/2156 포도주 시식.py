import sys
input = sys.stdin.readline
n = int(input())

wine = [[0, 0, 0] for _ in range(n)]
wine[0] = [0, int(input()), 0]

for i in range(1, n):
    k = int(input())
    wine[i][0] = max(wine[i-1])
    wine[i][1] = wine[i-1][0] + k
    wine[i][2] = wine[i-1][1] + k

print(max(wine[-1]))