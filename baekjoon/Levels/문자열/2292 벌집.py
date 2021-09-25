a = int(input())
i = 1
while True:
    if a == 1:
        break
    if 2 + 6 * ((i - 2) * (i - 1) / 2) <= a <= 1 + 6 * ((i - 1) * i / 2):
        break
    i += 1
print(i)
