n, m = map(int, input().split())
arr = list(map(int, input().split()))

moduler = [0] * 1001

for i in range(n):
    moduler[arr[i] % m] += 1
    tof = True

for i in range(1001):
    if moduler[i] > 1:
        tof = False

if tof == False:
    print(0)
else:
    ans = 1

    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = 0
            if arr[i] < arr[j]:
                tmp = arr[j] - arr[i]
            else:
                tmp = arr[i] - arr[j]
            ans *= tmp
            ans %= m

    print(ans % m)