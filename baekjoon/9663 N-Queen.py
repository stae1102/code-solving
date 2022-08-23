n = int(input())

flag_1 = [0] * n
flag_2 = [0] * (2 * n - 1)
flag_3 = [0] * (2 * n - 1)

cnt = 0


def nQueen(depth):
    global cnt
    if depth == n:
        cnt += 1
        return

    for i in range(n):
        if not(flag_1[i] or flag_2[i + depth] or flag_3[n + depth - i - 1]):
            flag_1[i], flag_2[i + depth], flag_3[n + depth - i - 1] = 1, 1, 1
            nQueen(depth + 1)
            flag_1[i], flag_2[i + depth], flag_3[n + depth - i - 1] = 0, 0, 0


nQueen(0)
print(cnt)
