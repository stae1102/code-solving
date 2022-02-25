a, b = map(int, input().split())
cnt = 0

while a >= b:
    
    while a % b != 0:
        a -= 1
        cnt += 1
    a //= b
    cnt += 1

while a > 1:
    a -= 1
    cnt += 1

print(cnt)