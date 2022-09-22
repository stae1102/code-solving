s = input().split()
a = int(s[0].replace(".", ""))
b = int(s[1])


def solve(n, s):
    if s == 1:
        return n
    else:
        if s % 2 == 1:
            return n * solve(n, s // 2) * solve(n, s // 2)
        else:
            return solve(n, s // 2) * solve(n, s // 2)


num = str(solve(a, b))
p = str((10 ** len(s[0].split(".")[1])) ** b)
idx = len(num) - len(p) + 1
if idx >= 0:
    print(num[:idx] + '.' + num[idx:])
else:
    print('0.' + '0' * (-idx) + num)
