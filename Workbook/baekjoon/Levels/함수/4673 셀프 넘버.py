def d() -> int:
    stack = []
    for i in range(1, 10001): 
        s = str(i)
        if i < 10: stack.append(i + (i % 10))
        elif i < 100: stack.append(i + (i // 10) + (i % 10))
        elif i < 1000: stack.append(i + (i // 100) + (int(s[1:]) // 10) + (i % 10))
        elif i <= 10000: stack.append(i + (i // 1000) + (int(s[1:]) // 100) + (int(s[2:]) // 10) + (i % 10))
        if i in stack:
            stack.remove(i)
            continue
        print(i)
d()

########## 우수 사례 ###########

import sys

def d(n: int):
    return n + n//1000 + (n%1000)//100 + (n%100)//10 + n%10

dList = [0]*10000
for n in range(10000):
    try:
        dList[d(n)] = 1
    except IndexError:
        continue

for d in range(10000):
    if dList[d]==0:
        print(d)
