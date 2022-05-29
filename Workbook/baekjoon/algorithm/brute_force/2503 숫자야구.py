import sys
input = sys.stdin.readline

n = int(input())
ans = [True] * 1001
cnt = 0
for i in range(n):
    num, s, b = map(int, input().split())
    num = str(num)
    for j in range(123, 988):
        j = str(j)
        if ('0' in j) or (j[0] == j[1] or j[1] == j[2] or j[2] == j[0]):
            ans[int(j)] = False
            continue
        s_cnt, b_cnt = 0, 0
        for x in range(3):
            for y in range(3):
                if j[x] == num[y]:
                    if x == y:
                        s_cnt += 1
                    else:
                        b_cnt += 1

        if ans[int(j)] and s_cnt == s and b_cnt == b:
            ans[int(j)] = True
        else:
            ans[int(j)] = False

for i in range(123, 988):
    if ans[i]:
        cnt += 1
print(cnt)