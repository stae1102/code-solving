import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
arr = sorted(input().split(), key=lambda x: int(x))
num = []
dict = {}


def solve(idx, cnt):
    if cnt == m:
        k = ' '.join(num)
        if k not in dict:
            dict[k] = 1
            print(k + '\n')
            return

    for i in range(idx, n):
        num.append(arr[i])
        solve(i + 1, cnt + 1)
        num.pop()


solve(0, 0)
