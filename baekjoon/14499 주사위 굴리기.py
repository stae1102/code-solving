import sys
import copy
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 동, 서, 북, 남의 순서
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# D1, D2, D3, D4, D5, D6
dice = [0, 0, 0, 0, 0, 0]


def move_direction(d):
    global dice
    new_dice = copy.deepcopy(dice)
    if d == 0:
        new_dice[1] = dice[4]
        new_dice[3] = dice[5]
        new_dice[4] = dice[3]
        new_dice[5] = dice[1]
    elif d == 1:
        new_dice[1] = dice[5]
        new_dice[3] = dice[4]
        new_dice[4] = dice[1]
        new_dice[5] = dice[3]
    elif d == 2:
        new_dice[0] = dice[3]
        new_dice[1] = dice[0]
        new_dice[2] = dice[1]
        new_dice[3] = dice[2]
    else:
        new_dice[0] = dice[1]
        new_dice[1] = dice[2]
        new_dice[2] = dice[3]
        new_dice[3] = dice[0]
    new_dice, dice = dice, new_dice


commands = list(map(int, input().split()))

for com in commands:
    nx = x + dx[com - 1]
    ny = y + dy[com - 1]
    if 0 <= nx < n and 0 <= ny < m:
        move_direction(com - 1)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[3]
        else:
            dice[3] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[1])
        x = nx
        y = ny
