def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b, k):
    return a * b // k


a, b = map(int, input().split())
k = gcd(a, b)
print(k)
print(lcm(a, b, k))
