n, s = map(int, input().split())
nums = sorted(map(int, input().split()))

ans = 0

def solve(idx, arr):
    global ans
    
    if arr and sum(arr) == s:
        ans += 1
    
    for i in range(idx, n):
        solve(i + 1, arr + [nums[i]])

    return

solve(0, [])

print(ans)