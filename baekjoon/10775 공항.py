import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[a] = b


g = int(input())
p = int(input())

gates = [i for i in range(g + 1)]
cnt = 0
for _ in range(p):
    k = int(input())
    dock = find_parent(gates, k)
    if dock != 0:
        union_parent(gates, dock, dock - 1)
    else:
        break
    cnt += 1

print(cnt)
