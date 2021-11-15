import sys
input = sys.stdin.readline
n = int(input())
graph = []
ans = []
mail = 0

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

def start_dfs(x, y):
    global mail
    mail = 0
    def dfs(x, y):
        global mail
        if x <= -1 or x >= n or y <= -1 or y >= n:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            mail += 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False
    return dfs(x, y)

result = 0
for i in range(n):
    for j in range(n):
        if start_dfs(i, j) == True:
            result += 1
            ans.append(mail)

print(result)

ans.sort()
for i in range(len(ans)):
    print(ans[i])
