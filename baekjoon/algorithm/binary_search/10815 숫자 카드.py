import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(num):
    pl = 0
    pr = n - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        if card[pc] == num:
            return 1
        elif card[pc] > num:
            pr = pc - 1
        else:
            pl = pc + 1
    return 0

for i in l:
    print(binary_search(i), end=' ')
