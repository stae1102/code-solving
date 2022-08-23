from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]

# 미네랄 체크
def check(x, y):
    if not (0 <= x < R and 0 <= y < C) or graph[x][y] == '.':
        return []
    q = deque([(x, y)])
    visited = [[0] * C for _ in range(R)]
    visited[x][y] = 1
    mineral = [(x, y)]

    while q:
        x, y = q.popleft()
        if graph[x][y] == '.':
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx; ny = y + dy
            if nx >= R:
                return []
            if nx >= 0 and 0 <= ny < C and not visited[nx][ny]:
                if graph[nx][ny] == 'x':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    mineral.append((nx, ny))

    return mineral

# 미네랄 떨어뜨리기
def fall(arr):
    MIN = 9887654321

    for x, y in arr:
        nx = x + 1 # 내려가면서 검사할 변수
        while nx < R: # 0보다 크거나 같을 동안
            if graph[nx][y] == 'x':
                if (nx, y) not in arr:
                    MIN = min(MIN, nx - x - 1)
                    break
            nx += 1
        else: MIN = min(MIN, nx - x - 1)

    arr.sort()
    while arr:
        x, y = arr.pop()
        graph[x][y] = '.'
        x += MIN
        graph[x][y] = 'x'

# 작대기 던지기
def stick(k, drt):
    if drt: # 방향이 오른쪽이면
        for i in range(C - 1, -1, -1):
            if graph[k][i] == 'x':
                graph[k][i] = '.'
                temp = check(k + 1, i) + check(k - 1, i) + check(k, i - 1)
                fall(temp)
                return

    else:
        for i in range(C):
            if graph[k][i] == 'x':
                graph[k][i] = '.'
                temp = check(k + 1, i) + check(k - 1, i) + check(k, i + 1)
                # print(temp)
                fall(temp)
                return

n = int(input())
sticks = list(map(int, input().split()))

direction = False
for i in sticks:
    stick(R - i, direction)
    direction = True if direction == False else False

for i in graph:
    print(''.join(i))