import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
s = [[] for _ in range(n)]
s[0] = [arr[0]]

idx = 0
for i in range(1, n):
    s[i] = [arr[i]]
    for j in range(i):
        if arr[j] < arr[i]:
            if d[i] < d[j] + 1:
                d[i] = d[j] + 1
                s[i] = s[j] + [arr[i]]
                if d[idx] < d[i]:
                    idx = i
            
print(d[idx])
print(*s[idx])
# print(s)