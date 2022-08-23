n = int(input())

flac_a = [False] * n
flac_b = [False] * (2 * n - 1)
flac_c = [False] * (2 * n - 1)

cnt = 0

def queen(depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    for i in range(n):
        if not (flac_a[i] or flac_b[i + depth] or flac_c[depth - i + n - 1]):
            flac_a[i] = flac_b[i + depth] = flac_c[depth - i + n - 1] = True
            queen(depth + 1)
            flac_a[i] = flac_b[i + depth] = flac_c[depth - i + n - 1] = False

queen(0)
print(cnt)