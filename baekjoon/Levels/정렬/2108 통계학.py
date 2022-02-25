import sys
import math
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    x = int(sys.stdin.readline())
    lst.append(x)

lst.sort()    # 정렬
cnt = [[None, 0] for _ in range(len(set(lst)))]    # 각 숫자에 대한 카운팅
idx = 0

for i in lst:
    while True:
        if cnt[idx][0] is None:    # 값이 정해지지 않다면 초기화
            cnt[idx][0] = i
            break
        elif cnt[idx][0] == i:    # 이미 있으면 += 1
            cnt[idx][1] += 1
            break
        else:
            idx += 1    # 값이 같지 않으면 다음 인덱스로

mode = max(cnt, key = lambda cnt: cnt[1])[1]
count = []

for i in cnt:
    if i[1] == mode:
        count.append(i[0])

print(math.ceil(sum(lst) / len(lst)) if (sum(lst) / len(lst)) % 1 >= 0.5 else round(sum(lst) / len(lst)))
print(lst[n // 2])
print(count[0] if len(count) == 1 else count[1])
print(lst[-1] - lst[0])

#########################################우수사례############################################

from sys import stdin


def sol2108():
    n = int(stdin.readline())
    counts = [0]*8001
    s = 0
    for i in stdin:
        num = int(i)
        counts[num+4000] += 1

    maxc = max(counts)
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001, -4001
    for i in range(8001):
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000
        s += num*counts[i]
        if cnt == maxc and mcnt < 2:
            mode = num
            mcnt += 1
        mi = min(mi, num)
        ma = max(ma, num)
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num

    print(round(s/n), med, mode, ma-mi, sep='\n')


if __name__ == '__main__':
    sol2108()
