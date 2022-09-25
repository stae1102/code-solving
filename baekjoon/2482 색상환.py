n = int(input())
k = int(input())
mod = 1000000003

# k번 선택했을 때의 n번째 인덱스가 가질 수 있는 경우의 수
d = [[-1] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    d[i][0] = 1
    d[i][1] = i


def find_color(n, k):
    if k > n / 2:
        d[n][k] = 0
        return 0

    if d[n][k] != -1:
        return d[n][k]
    else:
        d[n][k] = find_color(n - 1, k) % mod + find_color(n - 2, k - 1) % mod
        return d[n][k] % mod


print(find_color(n, k))
