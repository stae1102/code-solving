import sys

d = {}    # 변수가 워낙 다양하여 딕셔너리 사용

def w(a: int, b: int, c: int) -> None:
    try:
        if d[(a, b, c)]:    # 이미 딕셔너리에 존재하면 그 값을 반환
            return d[(a, b, c)]
    except:    # 딕셔너리에 없으면 딕셔너리에 값을 추가
        if a <= 0 or b <= 0 or c <= 0:
            d[(a, b, c)] = 1
            return 1
        elif a > 20 or b > 20 or c > 20:
            d[(a, b, c)] = w(20, 20, 20)
        elif a < b and b < c:
            d[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            d[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return d[(a, b, c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

###############################
########## 모범 사례 ##########
###############################

from sys import stdin


def sol9187():
    w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]    # 변수가 3개이기 때문에 3차원 리스트 구현
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
                else:
                    w[i][j][k] = w[i - 1][j][k] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]
    answer = []
    for i in stdin:
        a, b, c = map(int, i.split())
        if a == b == c == -1:
            break
        if a <= 0 or b <= 0 or c <= 0:
            answer.append(f'w({a}, {b}, {c}) = 1')
        elif a > 20 or b > 20 or c > 20:
            answer.append(f'w({a}, {b}, {c}) = {w[20][20][20]}')
        else:
            answer.append(f'w({a}, {b}, {c}) = {w[a][b][c]}')
    print('\n'.join(answer))


if __name__ == '__main__':
    sol9187()
