import sys
input = sys.stdin.readline
n, b = map(int, input().split())
con = []

if n == 0:
    con.append(n)

while n != 0:
    r = n % b
    if r >= 10:
        con.append(chr(55 + r))
    else:
        con.append(r)
    n //= b

for _ in range(len(con)):
    print(con.pop(), end='')
