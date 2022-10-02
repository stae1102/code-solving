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

graph = [[i] + list(map(int, input().split())) for i in range(n)]
cycle = [i for i in range(n)]
edges = []

for i in range(1, 4):
    tmp = sorted(graph, key=lambda x: x[i])
    for j in range(n - 1):
        cost = abs(tmp[j][i] - tmp[j + 1][i])
        edges.append((cost, tmp[j][0], tmp[j + 1][0]))

edges.sort()

ans = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(cycle, a) != find_parent(cycle, b):
        union_parent(cycle, a, b)
        ans += cost

print(ans)
