import sys
input = sys.stdin.readline
n = int(input())

d = [[0, 0, 0] for _ in range(n)]
k = int(input())
d[0] = [0, k, k]  # 쉬어가지 않았고, 처음 마시는 것이기 때문에 1번 인덱스에 저장

for i in range(1, n):
    k = int(input())
    d[i][0] = max(d[i - 1])  # 쉬어갈 때
    d[i][1] = d[i - 1][0] + k  # 첫 번째 마실 때
    d[i][2] = d[i - 1][1] + k  # 두 번째 마실 때

print(max(d[n - 1]))
