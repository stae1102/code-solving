# 재귀적으로 들어가야 함
# 먼저 별을 찍는 과정 나타내기
a = int(input())
arr = [[' ' for _ in range(a)] for _ in range(a)]

def star(n: int, x: int, y: int) -> str:
    """n: 변의 길이, x: 중간 좌표(x와 y는 동일)"""
    if n == 3: # 최소한의 수준일 때
        arr[y - 1][x - 1] = "*"
        arr[y - 1][x] = "*"
        arr[y - 1][x + 1] = "*"
        arr[y][x - 1] = "*"
        arr[y][x + 1] = "*"
        arr[y + 1][x - 1] = "*"
        arr[y + 1][x] = "*"
        arr[y + 1][x + 1] = "*"
    else:
        # 첫 번째 줄
        star(int(n / 3), x - int(n / 3), y - int(n / 3))
        star(int(n / 3), x, y - int(n / 3))
        star(int(n / 3), x + int(n / 3), y - int(n / 3))
        # 두 번째 줄
        star(int(n / 3), x - int(n / 3), y)
        star(int(n / 3), x + int(n / 3), y)
        # 세 번째 줄
        star(int(n / 3), x - int(n / 3), y + int(n / 3))
        star(int(n / 3), x, y + int(n / 3))
        star(int(n / 3), x + int(n / 3), y + int(n / 3))

star(a, int(a / 2), int(a / 2))

for i in range(a):
    for j in range(a):
        print(arr[i][j], end='')
    print()
