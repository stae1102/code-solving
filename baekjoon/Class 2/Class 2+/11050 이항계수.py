n, k = map(int, input().split())

def p(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * p(x - 1)

print(int(p(n) / (p(k) * p(n - k))))
