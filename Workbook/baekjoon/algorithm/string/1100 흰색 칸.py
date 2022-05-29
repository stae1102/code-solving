import sys
input = sys.stdin.readline

l = [list(input().rstrip()) for _ in range(8)]

def chess(i):
    white = 0
    if i % 2:
        for j in range(8):
            if j % 2 != 0 and l[i][j] == "F":
                white += 1
    else:
        for j in range(8):
            if j % 2 == 0 and l[i][j] == "F":
                white += 1
    return white

ans = 0

for i in range(8):
    ans += chess(i)

print(ans)
