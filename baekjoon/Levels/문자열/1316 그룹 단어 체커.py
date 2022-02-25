import sys
a = int(sys.stdin.readline())
l = [sys.stdin.readline().rstrip() for _ in range(a)]
count = 0
for i in l:
    s = [i[0]]
    for j in i[1:]:
        if (j in s) and (s[-1] != j):
            break
        s.append(j)
    else:
        count += 1
print(count)
