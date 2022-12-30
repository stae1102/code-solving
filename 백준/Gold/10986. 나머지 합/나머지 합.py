n, m = map(int, input().split())
arr = list(map(int, input().split()))

rest_count = { 0: 1 }
ans = 0

prefix_sum = [0] + arr
for i in range(1, n + 1):
  prefix_sum[i] = r = (prefix_sum[i] + prefix_sum[i - 1]) % m
  ans += rest_count.get(r, 0)
  rest_count[r] = rest_count.get(r, 0) + 1

print(ans)