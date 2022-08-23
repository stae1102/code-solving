def gcd(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b

    return b

n, m = map(int, input().split())
print(gcd(n, m))