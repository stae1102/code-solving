n, m, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
prefix_sum = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(2)]
color = ['W', 'B']

ans = -1

for x in range(1, n + 1):
  for y in range(1, m + 1):
    prefix_sum[0][x][y] += prefix_sum[0][x][y - 1] + prefix_sum[0][x - 1][y] - prefix_sum[0][x - 1][y - 1]
    prefix_sum[1][x][y] += prefix_sum[1][x][y - 1] + prefix_sum[1][x - 1][y] - prefix_sum[1][x - 1][y - 1]

    if board[x - 1][y - 1] == color[(x + y) % 2]:
      prefix_sum[0][x][y] += 1
    else:
      prefix_sum[1][x][y] += 1

for x in range(n - k + 1):
  for y in range(m - k + 1):
    min1 = prefix_sum[0][k + x][k + y] - prefix_sum[0][x][k + y] - prefix_sum[0][k + x][y] + prefix_sum[0][x][y]
    min2 = prefix_sum[1][k + x][k + y] - prefix_sum[1][x][k + y] - prefix_sum[1][k + x][y] + prefix_sum[1][x][y]
    ans = max(ans, min1, min2)

print(k * k - ans)