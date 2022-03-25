n, m = map(int, input().split())
pos = [i for i in range(1, n + 1)]    
flag = [False] * n

arr = []
def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(n):
        if flag[i]:
            continue
        flag[i] = True
        arr.append(pos[i])
        dfs(cnt + 1)
        arr.pop()
    
        for j in range(i + 1, n):
            flag[j] = False
    
dfs(0)
