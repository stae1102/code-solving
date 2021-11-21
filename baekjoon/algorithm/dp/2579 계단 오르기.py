import sys
input = sys.stdin.readline
n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

g = [0, 0]    # 다음으로 갈 수 없는 계단
h = [0, arr[1]]    # 다음으로 갈 수 있는 계단
for i in range(2, n + 1):
    g.append(h[i - 1] + arr[i])
    h.append(max(h[i - 2] + g[i - 2]) + arr[i])
print(max(g[n], h[n]))
