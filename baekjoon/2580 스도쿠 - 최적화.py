import sys
input = sys.stdin.readline


def fill_sudoku(cnt):
    if cnt == 0:
        for x in range(9):
            for y in range(9):
                print(sudoku[x][y], end=' ')
            print()
        exit()

    x, y = blanks[cnt - 1]

    for i in range(1, 10):
        if not (row[x][i] or col[y][i] or squ[x // 3 * 3 + y // 3][i]):
            row[x][i] = col[y][i] = squ[x // 3 * 3 + y // 3][i] = True
            sudoku[x][y] = i
            fill_sudoku(cnt - 1)
            row[x][i] = col[y][i] = squ[x // 3 * 3 + y // 3][i] = False
            sudoku[x][y] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
blanks = []
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
squ = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        k = sudoku[i][j]
        if k != 0:
            row[i][k] = True
            col[j][k] = True
            squ[i // 3 * 3 + j // 3][k] = True
        else:
            blanks.append((i, j))

fill_sudoku(len(blanks))
