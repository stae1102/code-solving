n, k = map(int, input().split())

a = 1
b = 1
mod = 1000000007

def pow(a, b):
    if b == 0: return 1
    if b % 2: return pow(a, b - 1) * a % mod
    half = pow(a, b // 2) % mod
    return half * half % mod

# n! 부분
for i in range(1, n + 1):
    a *= i
    a %= mod

# k! 부분
for i in range(1, k + 1):
    b *= i
    b %= mod

# (n - k)!부분
for i in range(1, (n - k) + 1):
    b *= i
    b %= mod

b = pow(b, mod-2) # B^(p - 2) 부분

ans = a * b % mod
print(ans)