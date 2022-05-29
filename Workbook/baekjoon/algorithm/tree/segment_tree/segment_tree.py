from math import ceil, log2
my_list = [i for i in range(11)]
tree = [0] * (pow(2, ceil(log2(len(list)) + 1)) - 1)

def init(left, right, node):
    if left == right:
        tree[node] = my_list[left]
        return
    else:
        mid = (left + right) // 2
        init(left, mid, node * 2)
        init(mid + 1, right, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return tree[node]
    if idx < left or right < idx:
        return 0
    else:
        mid = (left + right) // 2
        update(left, mid, node * 2, idx, value)
        update(mid + 1, right, node * 2 + 1, idx, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(left, right, node, lidx, ridx):
    global answer
    if ridx < left or right < lidx:
        return
    elif lidx <= left and right <= ridx:
        answer += tree[node]
        return
    elif lidx <= left or right <= ridx:
        mid = (left + right) // 2
        query(left, mid, node * 2, lidx, ridx)
        query(mid + 1, right, node * 2 + 1, lidx, ridx)
        return

answer = 0