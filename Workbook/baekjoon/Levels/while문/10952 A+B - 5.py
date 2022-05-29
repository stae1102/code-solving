import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0: break
    print(a + b)
    
#### 숏 코딩 ####
for a,_,b,_ in open(0):print(int(a)+int(b)or'')
