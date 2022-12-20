q = input().split('-')
ans = 0

for i in q[0].split('+'):
    ans += int(i)

for i in q[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)
