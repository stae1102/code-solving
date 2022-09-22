import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def human_to_num(human):
    global cnt
    if human not in number:
        number[human] = cnt
        parent.append([cnt, 1])
        cnt += 1
    return number[human]


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


t = int(input())

for _ in range(t):
    f = int(input())
    number = {}
    cnt = 0
    parent = []
    for i in range(f):
        a, b = map(human_to_num, input().rstrip().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        k = find_parent(parent, a)
        print(parent[k][1])
