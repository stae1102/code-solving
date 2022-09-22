import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x][0] != x:
        parent[x][0] = find_parent(parent, parent[x][0])
    return parent[x][0]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b][0] = a
        parent[a][1] += parent[b][1]
    else:
        parent[a][0] = b
        parent[b][1] += parent[a][1]


n, m = map(int, input().split())
parent = [[i, 1] for i in range(n + 1)]

for i in range(m):
    com, a, b = map(int, input().split())
    if com == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")
    print(parent)
