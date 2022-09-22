import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]


def cd(x, y, k):
    check = graph[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if check != graph[i][j]:
                print("(", end='')
                cd(x, y, k // 2)
                cd(x, y + k // 2, k // 2)
                cd(x + k // 2, y, k // 2)
                cd(x + k // 2, y + k // 2, k // 2)
                print(")", end='')
                return

    print(check, end="")
    return


cd(0, 0, n)
