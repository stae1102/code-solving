<<<<<<< HEAD
n, m = map(int, input().split())
num = sorted(map(int, input().split()))

arr = []

def bt(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(idx, len(num)):
        arr.append(num[i])
        bt(i + 1, cnt + 1)
        arr.pop()

=======
n, m = map(int, input().split())
num = sorted(map(int, input().split()))

arr = []

def bt(idx, cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(idx, len(num)):
        arr.append(num[i])
        bt(i + 1, cnt + 1)
        arr.pop()

>>>>>>> origin/ubuntu
bt(0, 0)