n, m = map(int, input().split())
num = sorted(input().split(), key=lambda x: int(x))

arr = []
dict = {}


def solve(cnt):
    if cnt == m:
        k = ' '.join(arr)
        if k not in dict:
            dict[k] = 1
            print(*arr)
        return

    for i in range(n):
        arr.append(num[i])
        solve(cnt + 1)
        arr.pop()


solve(0)
