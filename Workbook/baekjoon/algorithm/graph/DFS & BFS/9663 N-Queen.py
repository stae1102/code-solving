import sys
n = int(sys.stdin.readline())

flag_a = [False] * n
flag_b = [False for i in range(2 * n - 1)]
flag_c = [False for i in range(2 * n - 1)]

cnt = 0

def set(i):
    global flag_a, flag_b, flag_c
    if i == n:
        global cnt
        cnt += 1
        return
    for j in range(n):
        if(     not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + n - 1]):
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = True
            set(i + 1)
            flag_a[j] = flag_b[i + j] = flag_c[i - j + n - 1] = False

set(0)
print(cnt)
