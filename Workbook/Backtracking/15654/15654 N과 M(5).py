n, m = map(int, input().split())
num = list(sorted(map(int, input().split())))
is_num = [False] * n

arr = []

def bt(z):
    if z == m:
        print(*arr)
        return
    
    for i in range(n):
        if not is_num[i]:
            is_num[i] = True
            arr.append(num[i])
            bt(z + 1)
            is_num[i] = False
            arr.pop()

bt(0)