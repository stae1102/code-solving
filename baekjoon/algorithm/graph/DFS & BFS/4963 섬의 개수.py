import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            for dx, dy in d:
                dfs(x + dx, y + dy)
            return True
        return False
    
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    
    print(result)
