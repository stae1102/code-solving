def solve(idx, SUM):
    global ans
    if idx >= N:
        return
    SUM += nums[idx]
    if SUM == S:
        ans += 1
    solve(idx + 1, SUM - nums[idx])
    solve(idx + 1, SUM)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
solve(0, 0)
print(ans)
