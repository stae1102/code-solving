k = int(input())
s = [int(input().split()[1]) for _ in range(6)]
ans = []

for i in range(6):
    if i == 5:
        ans.append(s[-1] * s[0])
    else:
        ans.append(s[i] * s[i+1])

n = sum(ans) - 2 * max(ans)
print(n * k)