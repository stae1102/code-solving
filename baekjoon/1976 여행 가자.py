import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

cities = [i for i in range(n + 1)]

for i in range(1, n + 1):
    connect = list(map(int, input().split()))
    for j in range(n):
        if connect[j]:
            union_parent(cities, i, j + 1)

travel = list(map(int, input().split()))

tmp = travel[0]

for i in range(1, m):
    if find_parent(cities, tmp) != find_parent(cities, travel[i]):
        print("NO")
        break
else:
    print("YES")
