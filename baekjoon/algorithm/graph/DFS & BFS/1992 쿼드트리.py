import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def quad(x, y, n):
    check = graph[x][y]
    for a in range(x, x + n):
        for b in range(y, y + n):
            if check != graph[a][b]:
                print('(', end='')
                quad(x, y, n // 2)
                quad(x, y + n// 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
        
    if check == 0:
        print(0, end='')
        return
    else:
        print(1, end='')
        return

quad(0, 0, n)