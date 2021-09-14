import sys
while True:
    n = input()
    if n == ".":
        break
    stack = []
    if ("(" not in n) and ("[" not in n):
        if (")" in n) or ("]" in n):
            print("no")
            continue
        else:
            print("yes")
            continue
    elif (n.count("(") != (n.count(")"))) or ((n.count("[") != n.count("]"))):
        print("no")
        continue
    else:
        for j in n:
            if (j == "(") or (j == "["):
                stack.append(j)
            elif j == ")" and len(stack) != 0:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("no")
                    break
            elif j == "]" and len(stack) != 0:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    print("no")
                    break
        else:
            if stack: print("no")
            else:
                print("yes")
