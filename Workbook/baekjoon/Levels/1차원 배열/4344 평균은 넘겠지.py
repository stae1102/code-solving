import sys
a = int(sys.stdin.readline())
for i in range(a):
    n, *l = map(int, sys.stdin.readline().split())
    count = 0
    m = sum(l) / len(l)
    for j in l:
        if m < j: count += 1
    print(f"{count / n * 100:.3f}%")
