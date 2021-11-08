n, r, c = map(int, input().split())
n = 2 ** n

ans = 0

while n != 1:
    n //= 2
    if r >= n:    # 3, 4 분면
        r %= n
        if c >= n:    # 4 분면
            c %= n
            ans += (n ** 2) * 3
        else:    # 3 분면
            ans += (n ** 2) * 2
    else:    # 1, 2 분면
        if c >= n:    # 2 분면
            c %= n
            ans += (n ** 2)

print(ans)

#####################
##### 배열 사용 #####
#####################

N, r, c = map(int, input().split())

arr = [[None for _ in range(2 ** N)] for _ in range(2 ** N)]

def Z(n, k, x, y) -> None:    # * n: 배열의 행 및 열의 개수, k: 첫 시작 수
    arr[y][x] = k + 0
    arr[y][x + 2 ** (n - 1)] = k + 4 ** (n - 1)
    arr[y + 2 ** (n - 1)][x] = k + 4 ** (n - 1) * 2
    arr[y + 2 ** (n - 1)][x + 2 ** (n - 1)] = k + 4 ** (n - 1) * 3
    if n == 1:
        return
    Z(n - 1, k + 0, x, y)
    Z(n - 1, k + 4 ** (n - 1), x + 2 ** (n - 1), y)
    Z(n - 1, k + 4 ** (n - 1) * 2, x, y + 2 ** (n - 1))
    Z(n - 1, k + 4 ** (n - 1) * 3, x + 2 ** (n - 1), y + 2 ** (n - 1))

Z(N, 0, 0, 0)

print(arr[r][c])

##### 시간 복잡도 약간 줄인 코드 #####

N, r, c = map(int, input().split())

arr = [[None for _ in range(2 ** N)] for _ in range(2 ** N)]

def Z(n, k, x, y) -> None:    # * n: 배열의 행 및 열의 개수, k: 첫 시작 수
    arr[y][x] = k + 0
    arr[y][x + 2 ** (n - 1)] = k + 4 ** (n - 1)
    arr[y + 2 ** (n - 1)][x] = k + 4 ** (n - 1) * 2
    arr[y + 2 ** (n - 1)][x + 2 ** (n - 1)] = k + 4 ** (n - 1) * 3
    if arr[r][c]:
        print(arr[r][c])
        exit()
    if n == 1:
        return
    Z(n - 1, k + 0, x, y)
    Z(n - 1, k + 4 ** (n - 1), x + 2 ** (n - 1), y)
    Z(n - 1, k + 4 ** (n - 1) * 2, x, y + 2 ** (n - 1))
    Z(n - 1, k + 4 ** (n - 1) * 3, x + 2 ** (n - 1), y + 2 ** (n - 1))

Z(N, 0, 0, 0)
