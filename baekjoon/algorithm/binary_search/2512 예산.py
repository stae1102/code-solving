import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

pl = 1
pr = max(arr)

while pl <= pr:
    answer = 0
    pc = (pl + pr) // 2

    for i in arr:
        if i > pc:
            answer += pc
        else:
            answer += i

    if answer <= m:
        val = pc
        pl = pc + 1
    else:
        pr = pc - 1
    
print(val)
