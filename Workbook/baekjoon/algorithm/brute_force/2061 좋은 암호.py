n, m = map(int, input().split())

for i in range(2, m):
    if n % i == 0:
        print("BAD", i)
        exit()

print("GOOD")