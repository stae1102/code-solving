import sys
input = sys.stdin.readline

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def find_paper(x, y, n):
    global white, blue
    paper = color[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper != color[i][j]:
                find_paper(x, y, n // 2)
                find_paper(x + n // 2, y, n // 2)
                find_paper(x, y + n // 2, n // 2)
                find_paper(x + n // 2, y + n // 2, n // 2)
                return
    
    if paper == 0:
        white += 1
        return
    else:
        blue += 1
        return

find_paper(0, 0, n)
print(white)
print(blue)