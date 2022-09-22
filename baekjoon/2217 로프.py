import sys
input = sys.stdin.readline

n = int(input())

rope = sorted(map(int, sys.stdin.readlines()), reverse=True)

k = 0

for i in range(n):
    if k < rope[i] * (i + 1):
        k = rope[i] * (i + 1)

print(k)
