import sys
n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = map(int, input().split())
    floor = n % h if n % h != 0 else h
    number = n // h + 1 if n % h != 0 else n // h
    if number < 10:
        number = "0" + str(number)
    print(f'{floor}{number}')

#####################################################

