n = input()
strs = list(input())
cnt = 0
ans = 0
for i in strs:
    ans += (ord(i) - 96) * (31 ** cnt)
    cnt += 1
print(ans % 1234567891))
