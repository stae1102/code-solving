absence = set(i for i in range(1, 31))
for i in range(28):
    absence.remove(int(input()))

absence = sorted(absence)
print(*absence, sep='\n')
