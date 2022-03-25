n, m = map(int, input().split())

pos = [0] * m
flag = [False] * n

def track(k):
    for i in range(n):
        if not flag[i]:
            pos[k] = i + 1
            if k == m - 1:
                print(*pos)
            else:
                flag[i] = True
                track(k + 1)
                flag[i] = False

track(0)
