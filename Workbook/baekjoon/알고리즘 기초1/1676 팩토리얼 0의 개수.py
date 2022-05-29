import sys
n = int(sys.stdin.readline())
temp = 1

while n > 1:
    temp *= n
    n -= 1

cnt = 0
for i in range(len(str(temp)) - 1, -1, -1):
    if str(temp)[i] == "0":
        cnt += 1
    else:
        print(cnt)
        break
