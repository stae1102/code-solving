import sys
input = sys.stdin.readline
y, x = map(int, input().split())
lst = []
for i in range(y):
    lst.append(input().rstrip())
chess_board = [["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",    # 체크판이 가능한 가지수 미리 표현
               "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"],
               ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
               "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]]
# WBWBWBWB로 시작하는 체스판
sum_cnt = y * x    # 최대한으로 나올 수 있는 가지수

for i in chess_board: # 좌상단이 흰 색일 때와 검은 색일 때를 나누어서 판단
    for k in range(y - 7): # y축을 이동하는 횟수
        for l in range(x - 7): # x축을 이동하는 횟수
            cnt = 0 # 매번 필요한 정사각형을 입력
            for a in range(8): # 세로축을 8번
                for b in range(8): # 가로축을 8번
                    if lst[a + k][b + l] != i[a][b]:
                        cnt += 1
            if sum_cnt > cnt:
                sum_cnt = cnt
print(sum_cnt)
