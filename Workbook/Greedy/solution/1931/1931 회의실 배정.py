import sys
input = sys.stdin.readline

N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda dt: (dt[1], dt[0]))

cnt = 0
temp = 0

for i in range(N):
    if meeting[i][0] >= temp:
        temp = meeting[i][1]
        cnt += 1

print(cnt)
