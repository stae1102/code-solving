import sys
input = sys.stdin.readline

##################################
####### 에라토스테네스의 체 #######
##################################

MAX = 1000001
seive = [False] * 2 + [True] * (MAX - 2)
seive[4::2] = [False] * ((MAX - 1 - 2) // 2)
for i in range(3, int(MAX ** 0.5), 2):
    if seive[i]:
        seive[i * 2::i] = [False] * ((MAX - 1 - i) // i)

for _ in range(int(input())):
    n = int(input())
    part = 0
    h1, h2 = 2, n - 2
    while h1 <= h2:
        if seive[h1] and seive[h2]:
            part += 1
        if h1 == 2:
            h1 += 1
            h2 -= 1
        else:
            h1 += 2
            h2 -= 2
    print(part)
