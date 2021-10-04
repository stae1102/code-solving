import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])
lst.sort()
for i in lst:
    print(f"{i[0]} {i[1]}")
