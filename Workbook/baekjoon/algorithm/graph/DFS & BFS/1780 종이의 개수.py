import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

cnt = [0, 0, 0]

def find(k, x, y):

    temp = [0, 0, 0] # 0은 0 종이, 1은 1종이 2는 -1 종이
    for i in range(k):
        for j in range(k):
            temp[paper[x + i][y + j]] += 1

    union = False
    
    for i in range(3):
        if temp[i] == k ** 2:
            union = True
            cnt[i] += 1
    
    # if union:
    #     for i in range(k):
    #         cnt[i] += temp[i]
    
    
    # if union:
    # if k == 3:
    #     print(f'----------{k}----------')
    #     for i in range(k):
    #         for j in range(k):
    #             print(paper[x + i][y + j], end=' ')
    #         print()
    #     print(temp, x, y)

    next = k // 3
    if next and not union:
        find(next, x, y)
        find(next, x + next, y)
        find(next, x + 2 * next, y)
        find(next, x, y + next)
        find(next, x + next, y + next)
        find(next, x + 2 * next, y + next)
        find(next, x, y + 2 * next)
        find(next, x + next, y + 2 * next)
        find(next, x + 2 * next, y + 2 * next)

find(n, 0, 0)

print(cnt[-1])
print(cnt[0])
print(cnt[1])