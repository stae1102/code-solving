from sys import stdin

n = int(stdin.readline())

stack = [1]
cnt = 1
ans = "+"

num = int(stdin.readline())

while cnt != n + 1:
    if not stack or stack[-1] < num:
        cnt += 1
        stack.append(cnt)
        ans += "+"
    elif stack[-1] == num:
        stack.pop()
        ans += "-"
        if cnt == n and not stack:
            break
        num = int(stdin.readline())
    else:
        print("NO")
        exit()

print("\n".join(ans))