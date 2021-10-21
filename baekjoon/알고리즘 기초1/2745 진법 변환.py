import sys
n, b = sys.stdin.readline().split()
a = [1, 2, 3, 4, 5]
decimal = 0

for i in range(len(n) - 1, -1, -1):
    if n[i].isalpha():
        decimal += (int(b) ** (len(n) - 1 - i)) * (ord(n[i]) - 55)
    else:
        decimal += (int(b) ** (len(n) - 1 - i)) * int(n[i])

print(decimal)
