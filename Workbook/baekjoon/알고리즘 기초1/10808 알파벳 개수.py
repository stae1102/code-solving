strs = input()
cnt = {chr(96 + i):0 for i in range(1, 27)}
for str in strs:
    cnt[str] += 1
print(*cnt.values())
