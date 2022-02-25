import sys

def gcd(x, y):    # 유클리드 호제법
    while y != 0:
        x, y = y, x % y
    return x

for i in range(int(sys.stdin.readline())):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for j in range(1, len(arr) - 1):    # 브루트포스법
        for k in range(j + 1, len(arr)):
            ans += gcd(arr[j], arr[k])
    print(ans)
