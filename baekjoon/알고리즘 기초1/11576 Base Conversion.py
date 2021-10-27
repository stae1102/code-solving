import sys
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dec = 0

for i in range(len(num)):
    dec += num.pop() * (a ** i)

ans = []

while dec != 0:
    r = dec % b
    ans.append(r)
    dec //=b

for _ in range(len(ans)):
    print(ans.pop(), end=' ')
