import sys
sys.setrecursionlimit(10**6)
div = 1000000

arr = sys.stdin.readline().rstrip()
l = len(arr) - 1
d = [0] * (l + 1)


def encrypt(i):
    if i > l:
        return 1

    if d[i] != 0:
        return d[i]

    if arr[i] != "0":
        d[i] += encrypt(i + 1) % div
        if i + 1 <= l:
            if int(arr[i:i + 2]) <= 26:
                d[i] += encrypt(i + 2) % div
    else:
        return 0

    return d[i] % div


print(encrypt(0))
