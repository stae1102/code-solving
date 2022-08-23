from sys import stdin
input = stdin.readline


def lotto(arr, idx, depth):
    if depth == 6:
        k = ' '.join(tmp)
        if k not in visited:
            # print(visited)
            visited[k] = 1
            print(k)
        return

    for i in range(idx, int(n)):
        tmp.append(arr[i])
        lotto(arr, i + 1, depth + 1)
        tmp.pop()


while True:
    n, *k = input().split()
    if n == "0":
        break
    visited = dict()
    tmp = []
    lotto(k, 0, 0)
    print()
