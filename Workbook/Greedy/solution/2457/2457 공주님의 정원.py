import sys
input = sys.stdin.readline

N = int(input())
F = [[] for _ in range(N)]
month = [i for i in range(1, 13)]
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def diff(fm, fd, lm, ld):
    day_diff = 0
    if fm == lm:
        day_diff = ld - fd
    else:
        day_diff += day[fm - 1] - fd + ld
        fm += 1
        while fm < lm:
            day_diff += day[fm - 1]
            fm += 1
    return day_diff

# fm: First Month, fd: first Day
# lm: Last Month, ld: Last Day
for i in range(N):
    fm, fd, lm, ld = map(int, input().split())
    day_diff = diff(fm, fd, lm, ld)
    F[i] = [day_diff, fm, fd, lm, ld]
F.sort(key = lambda x: (x[1], x[2], -x[0], x[3], x[4]))

'''
def find_first_flower(flowers):
    month_day = [0, 0]
    idx = 0
    for i in range(N):
        flower = flowers[i]
        if flower[0] > 2:
            break
        if month_day[0] <= flower[0]:
            if month_day[1] < flower[1]:
                month_day = flower
                idx = i
    
    return month_day
'''

# fm, fd = find_first_flower(F)
        
print(F)