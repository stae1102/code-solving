import sys
input = sys.stdin.readline

n = int(input())

rooms = [list(map(int, input().split())) for _ in range(n)]
rooms.sort(key=lambda x: (x[1], x[0]))

cnt = 0
k = 0

for i in range(n):
    if rooms[i][0] < k:
        continue
    else:
        k = rooms[i][1]
        cnt += 1

print(cnt)
