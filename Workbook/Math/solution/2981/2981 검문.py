import sys
input = sys.stdin.readline

n = int(input())
l = sorted([int(input()) for _ in range(n)])
re_l = []

for i in range(1, n):
    re_l.append(l[i] - l[i-1])

def gcd(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    return b

GCD = re_l[0]
for i in range(1, len(re_l)):
    GCD = gcd(GCD, re_l[i])

result = set()
for i in range(2, int(GCD ** 0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))