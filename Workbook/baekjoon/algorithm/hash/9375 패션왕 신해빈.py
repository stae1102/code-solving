from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())

def solve():
    cloth = {}
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if b in cloth:
            cloth[b] += [a]
        else:
            cloth[b] = [a]

    ans = 1
    for i in cloth.values():
        ans *= len(i) + 1
    print(ans - 1)

for _ in range(t):
    solve()