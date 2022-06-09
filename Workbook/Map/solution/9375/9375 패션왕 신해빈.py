import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    cloth = {}
    n = int(input())
    ans = 1

    for _ in range(n):
        name, kind = input().split()
        if kind in cloth:
            cloth[kind] += [name]
        else:
            cloth[kind] = [name]
    
    for val in cloth.values():
        ans *= len(val) + 1
    
    print(ans - 1)