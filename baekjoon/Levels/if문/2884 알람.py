a, b = list(map(int, input().split()))
if b - 45 < 0:
    b = 60 + b - 45
    a -= 1
    if a < 0: a = 23
else:
    b -= 45
print(f'{str(a)} {str(b)}')
