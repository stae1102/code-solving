import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b = sorted(b, reverse=True)

for i in range(n):
    a[i] = a[i] * b[i]
print(sum(a))

#############################
######### 계수정렬 ##########
#############################

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

def count_sort(x):
    count = [0] * (max(x) + 1)

    for i in range(len(x)):
        count[x[i]] += 1
    x = []

    for i in range(len(count)):
        for _ in range(count[i]):
            x.append(i)
    return x

a = count_sort(a)
b = count_sort(b)
b.reverse()

for i in range(n):
    a[i] = a[i] * b[i]
print(sum(a))
