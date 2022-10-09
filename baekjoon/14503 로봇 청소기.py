from collections import deque
import sys
input = sys.stdin.readline

'''
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
  1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
  2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
  3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
  4. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''


def bfs(r, c, d):
    # 청소 구역 테이블
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((r, c, d))
    visited[r][c] = True
    cnt = 1

    while q:
        x, y, d = q.popleft()
        for i in range(1, 5):  # 4까지 도달했을 때, 비로소 2-3, 2-4 조건으로 넘어감
            nd = (d + i) % 4  # 방향 계산
            nx = x + dx[nd]
            ny = y + dy[nd]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny, nd))
                break
        else:  # 4방향 모두 불가능
            if graph[x - dx[d]][y - dy[d]] != 1:
                q.append((x - dx[d], y - dy[d], d))

    return cnt


# n: 세로, m: 가로
n, m = map(int, input().split())

# r: x좌표, c: y좌표, d: 방향
r, c, d = map(int, input().split())

if d == 1:
    d = 3
elif d == 3:
    d = 1

# 0: 북, 1: 서, 2: 남, 3: 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 지도
graph = [list(map(int, input().split())) for _ in range(n)]

# 청소 시작
print(bfs(r, c, d))
