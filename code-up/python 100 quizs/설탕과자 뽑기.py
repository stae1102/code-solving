n = list(map(int, (input().split()))) # 좌표 설정
w = [[0 for i in range(n[1])]for j in range(n[0])]
a = int(input()) # 막대를 놓을 횟수

for i in range(a): #a번 반복
    l, d, x, y = tuple(map(int, input().split())) # 방향이 분기점이 되어야 함
    if d: # d가 세로일 때
        for _ in range(l):
            w[x-1][y-1] = 1
            x += 1
    else:
        for _ in range(l):
            w[x-1][y-1] = 1
            y += 1

for i in range(n[0]):
    for j in range(n[1]):
        print(w[i][j], end=' ')
    print()
