import sys
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
cnt = list(map(int, sys.stdin.readline().split()))

def bin_search(l, key):
    pl = 0
    pr = len(lst) - 1
    while True:
        pc = (pl + pr) // 2
        if l[pc] == key:
            return 1
        elif l[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

for i in cnt:
    print(bin_search(lst, i))
    
#############################

import sys
n = sys.stdin.readline()
lst = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
cnt = list(map(int, sys.stdin.readline().split()))


for i in cnt:
    print(1 if i in lst else 0)
