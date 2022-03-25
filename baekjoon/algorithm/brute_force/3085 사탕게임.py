import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

ans = 0

def check():
    # 행 체크
    curr = 0
    for i in range(n):
        candies = 1
        for j in range(1, n):
            if graph[i][j - 1] == graph[i][j]:
                candies += 1
                curr = max(curr, candies)
            else:
                candies = 1
    
    for i in range(n):
        candies = 1
        for j in range(1, n):
            if graph[j - 1][i] == graph[j][i]:
                candies += 1
                curr = max(curr, candies)
            else:
                candies = 1
    
    return curr

for i in range(n):
    for j in range(n):
        # 오른쪽 캔디와 바꾸기
        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            ans = max(ans, check())
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
        # 아래쪽 캔디와 바꾸기
        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            ans = max(ans, check())
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

print(ans)