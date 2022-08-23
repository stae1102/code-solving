from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = []

# 맵 입력 및 상어 위치 출력
for i in range(N):
    a = list(map(int, input().split()))
    if 9 in a: shark = [i, a.index(9)] # x, y, 크기, 먹은 물고기
    board.append(a)

# 나머지 로직은 다 맞는데, 최단거리 물고기를 찾지 못함 ㅠㅠ 다시 로직 작성하기.
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

size = 2
ate = 0
ans = 0

def find_fish(x, y):
    global size, ate
    arr = []
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    q = deque([(x, y, 0)])

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if size < board[nx][ny]:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
                if size > board[nx][ny] and board[nx][ny]:
                    arr.append((cnt + 1, nx, ny))

    # 물고기를 먹은 경우
    if arr:
        if ate + 1 == size:
            ate = 0
            size += 1
        else:
            ate += 1

        MIN = min(arr)
        board[MIN[1]][MIN[2]] = 0
        return MIN[0], MIN[1], MIN[2]

    # 물고기를 먹지 못한 경우
    else:
        return 0, 0, 0

def bfs(x, y):
    global ans

    # x, y는 시작지점
    q = deque()
    q.append((x, y)) # x좌표, y좌표, 이동 횟수

    while q:
        x, y = q.popleft()
        cnt, x, y = find_fish(x, y)
        # 물고기를 먹었을 때, 이동한 거리만큼 추가
        if cnt:
            ans += cnt
            q.append((x, y)) # 다음 상어 로직 시작 위치
    
    # 아무 물고기도 못 먹은 경우에는 0 출력
    if ans == 0:
        return 0
    else:
        return ans

board[shark[0]][shark[1]] = 0
print(bfs(shark[0], shark[1]))