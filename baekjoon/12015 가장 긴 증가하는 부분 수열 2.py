import sys
input = sys.stdin.readline


def binary_search(arr, k):
    pl, pr = 0, len(arr) - 1
    while pl <= pr:
        mid = (pl + pr) // 2

        if arr[mid] < k:
            pl = mid + 1
        else:
            pr = mid - 1
    return pl


n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]

for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = binary_search(dp, a[i])
        dp[idx] = a[i]

print(len(dp))
