# 백준 10994
# 2차원 리스트로 먼저 배열 설정
n = int(input())
arr = [[' ' for _ in range(n * 4 -3)] for _ in range(n * 4 - 3)]
def star(n: int, x: int, y: int) -> None:
    """n: 개수, x: 정중앙 x좌표, y: 정중앙 y좌표"""
    if n == 1:
        arr[y][x] = "*"
    else:
        # 가로
        for i in range(n * 4 -3):
            arr[y - (n * 2 - 2)][x - (n * 2 - 2) + i] = "*"
        # 세로
        for i in range(n * 4 - 3):
            arr[y - (n * 2 - 2) + i][x - (n * 2 - 2)] = "*"
            arr[y - (n * 2 - 2) + i][x + (n * 2 - 2)] = "*"
        # 가로
        for i in range(n * 4 -3):
            arr[y + (n * 2 - 2)][x - (n * 2 - 2) + i] = "*"
        star(n - 1, x, y)

star(n, n * 2 - 2, n * 2 - 2)

for i in range(n * 4 - 3):
    for j in range(n * 4 - 3):
        print(arr[i][j], end='')
    print()
