import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(key = lambda lst: (lst[1], lst[0]))
for i in lst:
    print(f"{i[0]} {i[1]}")
