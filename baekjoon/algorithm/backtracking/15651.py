import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pos = [i for i in range(1, n + 1)]

arr = []
def dfs(cnt):
    if cnt == m:    # cnt가 충족되면 프린트
        print(*arr)
        return
    
    for i in range(n):    # 굳이 flag를 세울 필요가 없음
        arr.append(pos[i])
        dfs(cnt + 1)
        arr.pop()
        
dfs(0)
