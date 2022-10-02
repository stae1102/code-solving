import sys
import copy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def go_up(graph):
    graph = copy.deepcopy(graph)
    processed = [[False] * n for _ in range(n)]

    for y in range(n):
        for x in range(1, n):
            if graph[x][y] != 0:
                while x > 0 and graph[x - 1][y] == 0:
                    graph[x][y], graph[x - 1][y] = graph[x - 1][y], graph[x][y]
                    x -= 1
                if x > 0 and graph[x - 1][y] == graph[x][y]:  # x == 0이면 마지막 인덱스와 비교함
                    if not processed[x - 1][y]:  # 만약 한 번도 안 합쳤었다면
                        processed[x - 1][y] = True
                        graph[x - 1][y] += graph[x][y]
                        graph[x][y] = 0

    return graph


def go_left(graph):
    graph = copy.deepcopy(graph)
    processed = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(1, n):
            if graph[x][y] != 0:
                while y > 0 and graph[x][y - 1] == 0:
                    graph[x][y], graph[x][y - 1] = graph[x][y - 1], graph[x][y]
                    y -= 1
                if y > 0 and graph[x][y - 1] == graph[x][y]:
                    if not processed[x][y - 1]:
                        processed[x][y - 1] = True
                        graph[x][y - 1] += graph[x][y]
                        graph[x][y] = 0

    return graph


def go_right(graph):
    graph = copy.deepcopy(graph)
    processed = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n - 2, -1, -1):
            if graph[x][y] != 0:
                while y < n - 1 and graph[x][y + 1] == 0:
                    graph[x][y + 1], graph[x][y] = graph[x][y], graph[x][y + 1]
                    y += 1
                if y < n - 1 and graph[x][y + 1] == graph[x][y]:
                    if not processed[x][y + 1]:
                        processed[x][y + 1] = True
                        graph[x][y + 1] += graph[x][y]
                        graph[x][y] = 0

    return graph


def go_down(graph):
    graph = copy.deepcopy(graph)
    processed = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n - 2, -1, -1):
            if graph[x][y] != 0:
                while x < n - 1 and graph[x + 1][y] == 0:
                    graph[x + 1][y], graph[x][y] = graph[x][y], graph[x + 1][y]
                    x += 1
                if x < n - 1 and graph[x + 1][y] == graph[x][y]:
                    # print(graph, x, y, x + 1, y)
                    if not processed[x + 1][y]:
                        processed[x + 1][y] = True
                        graph[x + 1][y] += graph[x][y]
                        graph[x][y] = 0

    return graph


ans = -1


def solve(cnt, graph):
    global ans
    if cnt == 5:
        # print(graph)
        ans = max(ans, max(map(max, graph)))
        return

    solve(cnt + 1, go_left(graph))
    solve(cnt + 1, go_right(graph))
    solve(cnt + 1, go_up(graph))
    solve(cnt + 1, go_down(graph))


solve(0, board)
print(ans)
