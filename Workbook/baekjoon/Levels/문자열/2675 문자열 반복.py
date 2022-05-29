import sys
a = int(sys.stdin.readline())
for i in range(a):
    n, l =  sys.stdin.readline().rstrip().split()
    for i in l:
        print(i * int(n), end='')
    print()
