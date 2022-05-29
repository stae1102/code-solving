a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
b = input()

for i in a:
    if i in b:
        b = b.replace(i, '_')

print(len(b))
