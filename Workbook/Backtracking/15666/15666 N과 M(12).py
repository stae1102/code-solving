n, m = map(int, input().split())
num = sorted(input().split(), key=lambda x: int(x))

arr = []
dict = {}


def solve(idx, cnt):
    if cnt == m:
        k = ' '.join(arr)
        if k not in dict:
            dict[k] = 1
            print(k)
        return

    for i in range(idx, n):
        arr.append(num[i])
        solve(i, cnt + 1)
        arr.pop()


solve(0, 0)
