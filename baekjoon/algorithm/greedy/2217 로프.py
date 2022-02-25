import sys
input = sys.stdin.readline
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

w = 0
for i in range(1, n + 1):
    if w < arr[i - 1] * i:
        w = arr[i - 1] * i

print(w)
