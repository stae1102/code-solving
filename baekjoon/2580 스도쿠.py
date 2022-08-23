import sys
input = sys.stdin.readline


def is_valid(x, y, k):
    if k in sudoku[x]:
        return False

    for s in sudoku:
        if s[y] == k:
            return False

    co_x, co_y = x // 3, y // 3
    for c in sudoku[co_x * 3:co_x * 3 + 3]:
        if k in c[co_y * 3:co_y * 3 + 3]:
            return False

    return True


def fill_sudoku(cnt):
    if cnt == 0:
        for x in range(9):
            for y in range(9):
                print(sudoku[x][y], end=' ')
            print()
        exit()

    x, y = blanks[cnt - 1]

    for i in range(1, 10):
        if is_valid(x, y, i):
            sudoku[x][y] = i
            fill_sudoku(cnt - 1)
            sudoku[x][y] = 0


sudoku = []
blanks = []

for i in range(9):
    line = list(map(int, input().split()))
    sudoku.append(line)
    for j in range(9):
        if line[j] == 0:
            blanks.append((i, j))

fill_sudoku(len(blanks))
