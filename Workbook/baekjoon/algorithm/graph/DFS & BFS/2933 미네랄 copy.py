# https://www.acmicpc.net/source/36477990 참고하여 재제출

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미네랄 체크
def check(y, x):
    if y == R:
        return False
    
    visited = [[0] * C for _ in range(R)]
    visited[y][x] = 1
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny == R: # 바닥에 닿으면 붙어있는 미네랄임
                return False
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                if graph[ny][nx] == 'x':
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    
    return True

# 미네랄 떨어뜨리기
def fall(y, x):
    cluster = [(y, x)]
    graph[y][x] = '.'
    q = deque(cluster)
    visited = [[0] * C for _ in range(R)]
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                if graph[ny][nx] == 'x':
                    visited[ny][nx] = 1
                    cluster.append((ny, nx))
                    graph[ny][nx] = '.'
                    q.append((ny, nx))
    
    drop = 0
    lowest = False
    while not lowest:
        for y, x in cluster:
            ny = y + drop
            if ny == R or graph[ny][x] == 'x':
                lowest = True
                break
        else:    
            drop += 1
    drop -= 1

    for y, x in cluster:
        ny = y + drop
        graph[ny][x] = 'x'

# 작대기 던지기
def stick(k, direction):
    if not direction: # 왼 -> 오
        for i in range(C):
            if graph[k][i] == 'x':
                graph[k][i] = '.'
                return i

    else: # 오 -> 왼
        for i in range(C - 1, -1, -1):
            if graph[k][i] == 'x':
                graph[k][i] = '.'
                return i
    
    # 헛방
    return -1

n = int(input())
sticks = list(map(int, input().split()))

direction = 0
for i in sticks:
    hit_y = R - i
    hit_x = stick(hit_y, direction)
    direction = (direction + 1) % 2

    if hit_x == -1:
        continue

    # 작대기 던진 후 미네랄들을 검사하기 위해 큐에 저장
    mineral = []
    for i in range(4):
        nx = hit_x + dx[i]
        ny = hit_y + dy[i]
        if 0 <= ny < R and 0 <= nx < C:
            if graph[ny][nx] == 'x':
                mineral.append((ny, nx))

    # 미네랄 검사
    for y, x in mineral:
        if check(y, x):
            fall(y, x)
            break

for i in graph:
    print(''.join(i))