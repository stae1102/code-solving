import sys
n = int(sys.stdin.readline())
sub = 0
max_num = 0
max_l = []
while sub <= n:
    l = [n]
    l.append(n - sub)
    while n > 0 and l[-2] >= l[-1] and (l[-2] >= 0 or l[-1] >= 0):
        l.append(l[-2] - l[-1])
    if max_num < len(l):
        max_num = len(l)
        max_l = l
    sub += 1
print(max_num)
print(*max_l)
