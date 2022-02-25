s = input()
i = 0
for j in range(len(s)):
    i += 1
    if i == 10:
        i = 0
        print(s[j], end='\n')
    else:
        print(s[j], end="")
