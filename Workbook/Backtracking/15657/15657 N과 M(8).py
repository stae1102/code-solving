n, m = map(int, input().split())
num = sorted(map(int, input().split()))

arr = []

def bt(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(idx, len(num)):
        arr.append(num[i])
        bt(i, cnt + 1)
        arr.pop()

bt(0, 0)