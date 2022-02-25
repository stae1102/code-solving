strs = input()
l = []
for i in range(len(strs)):
    l.append(strs[i:])
l.sort()
print(*l, sep="\n")
