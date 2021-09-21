import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
min = b[0]
max = b[0]

for i in b[1:]:
    if i < min:
        min = i
    elif i > max:
        max = i

print(min, max)

######## 개선 ########

'''
★★★ 가변 인자를 사용하는 방법 ★★★
'''

import sys
n, *x = map(int, sys.stdin.read().split())
print(min(x), max(x))
