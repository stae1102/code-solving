from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [(list(map(int, input().rstrip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]    # 방문기록 설정/ [0, 0] 0번 인덱스 -> 안 부신 상태, 1번 인덱스 -> 부신 상태
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

####################
##### bfs구현 ######
####################

def bfs(x, y, w):
    queue = deque()
    cnt = 1    # 시작과 함께 count 설정
    queue.append((cnt, x, y, w))
    while queue:
        cnt, x, y, w = queue.popleft()    # bfs
        visited[x][y][w] = 1    # 방문 설정

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny][w] == 1:    # 벽을 부순 곳을 다시 방문하는 경우, [x][y][w]는 0인 상태로 방문하는 것이기 때문에(벽을 부순 적이 없을 때) 계속해서 진행이 가능하다.
                continue
            if graph[nx][ny] == 0 or (graph[nx][ny] == 1 and w == 0):
                visited[nx][ny][w] = 1    # 다음 번 방문 설정
                if graph[nx][ny] == 1:
                    queue.append((cnt + 1, nx, ny, w + 1))
                else:
                    queue.append((cnt + 1, nx, ny, w))
    return -1

print(bfs(0, 0, 0))
