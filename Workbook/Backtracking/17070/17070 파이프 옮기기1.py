<<<<<<< HEAD
import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
pipe = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
pipe[0][1][0] = 1
for i in range(1, n - 1):
	if house[0][i + 1]:
		break
	pipe[0][i + 1][0] = pipe[0][i][0]
for i in range(1, n):
	for j in range(1, n):
		if house[i][j]:
			continue
		pipe[i][j][0] = pipe[i][j - 1][0] + pipe[i][j - 1][1]
		pipe[i][j][2] = pipe[i - 1][j][1] + pipe[i - 1][j][2]
		if house[i - 1][j] or house[i][j - 1]:
			continue
		pipe[i][j][1] = sum(pipe[i - 1][j - 1])
print(sum(pipe[n - 1][n - 1]))

'''
import sys
n = int(sys.stdin.readline())
graph = [['0'] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    graph[i][1:-1] = sys.stdin.readline().rstrip().split()

if graph[n][n] == '1':
    print(0)
    exit()

ans = 0

# 0 = 가로, 1 = 대각선, 2 = 세로
def pipe(x, y, direction):
    global ans
    
    if x > n or y > n:
        return

    if x == n and y == n:
        ans += 1

    if graph[x + 1][y] != '1' and (direction == 1 or direction == 2):
        pipe(x + 1, y, 2)
    
    if graph[x + 1][y + 1] != '1' and graph[x + 1][y] != '1' and graph[x][y + 1] != '1':
        pipe(x + 1, y + 1, 1)
    
    if graph[x][y + 1] != '1' and (direction == 1 or direction == 0):
        pipe(x, y + 1, 0)

pipe(1, 2, 0)

print(ans)
=======
import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
pipe = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
pipe[0][1][0] = 1
for i in range(1, n - 1):
	if house[0][i + 1]:
		break
	pipe[0][i + 1][0] = pipe[0][i][0]
for i in range(1, n):
	for j in range(1, n):
		if house[i][j]:
			continue
		pipe[i][j][0] = pipe[i][j - 1][0] + pipe[i][j - 1][1]
		pipe[i][j][2] = pipe[i - 1][j][1] + pipe[i - 1][j][2]
		if house[i - 1][j] or house[i][j - 1]:
			continue
		pipe[i][j][1] = sum(pipe[i - 1][j - 1])
print(sum(pipe[n - 1][n - 1]))

'''
import sys
n = int(sys.stdin.readline())
graph = [['0'] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    graph[i][1:-1] = sys.stdin.readline().rstrip().split()

if graph[n][n] == '1':
    print(0)
    exit()

ans = 0

# 0 = 가로, 1 = 대각선, 2 = 세로
def pipe(x, y, direction):
    global ans
    
    if x > n or y > n:
        return

    if x == n and y == n:
        ans += 1

    if graph[x + 1][y] != '1' and (direction == 1 or direction == 2):
        pipe(x + 1, y, 2)
    
    if graph[x + 1][y + 1] != '1' and graph[x + 1][y] != '1' and graph[x][y + 1] != '1':
        pipe(x + 1, y + 1, 1)
    
    if graph[x][y + 1] != '1' and (direction == 1 or direction == 0):
        pipe(x, y + 1, 0)

pipe(1, 2, 0)

print(ans)
>>>>>>> origin/ubuntu
'''