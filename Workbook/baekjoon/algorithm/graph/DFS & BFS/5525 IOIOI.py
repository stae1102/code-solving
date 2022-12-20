import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

cnt = 0
check = 0
i = 1
while i < m - 1:
    if s[i-1] == "I" and s[i] == "O" and s[i + 1] == "I":
        check += 1
        if check == n:
            cnt += 1
            check -= 1
        i += 1
    else:
        check = 0
    i += 1

print(cnt)