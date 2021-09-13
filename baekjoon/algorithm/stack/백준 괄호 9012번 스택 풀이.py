a = int(input())

for i in range(a):
    stack = []
    k = input()
    if (k[0] == ')') or (k[-1] == '(') or (k.count('(') != k.count(')')):
        print("NO")
        continue
    for j in k:
        if j == "(": stack.append("(")
        else: # ")"일 때,
            if stack: stack.pop()
            else:
                print("NO")
                break
    else: print("YES")
