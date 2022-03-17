import sys
input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]
array.sort()

ans = 0

for x in range(n):
    temp = int(1e9)
    for a in range(n):
        if array[x][1] == array[a][1] and a != x:
            temp = min(temp, abs(array[x][0] - array[a][0]))
    ans += temp

print(ans)