n = int(input())
k, *rings = map(int, input().split())

def findGCD(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    return b

for i in range(n - 1):
    gcd = findGCD(k, rings[i])
    print(f'{k // gcd}/{rings[i] // gcd}')