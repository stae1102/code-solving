n, m = map(int, input().split())
arr = list(map(int, input().split()))

rest_count = { 0: 1 }
ans = 0

prefix_sum = [0] + arr
for i in range(1, n + 1):
  prefix_sum[i] += prefix_sum[i - 1]
  prefix_sum[i] %= m
  if prefix_sum[i] in rest_count:
    ans += rest_count[prefix_sum[i]]
    rest_count[prefix_sum[i]] += 1
  else:
    rest_count[prefix_sum[i]] = 1

print(ans)