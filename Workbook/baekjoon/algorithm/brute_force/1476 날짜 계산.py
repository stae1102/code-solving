import sys

ans = list(map(int, sys.stdin.readline().split()))

esm = [0, 0, 0]
year = 0

while ans != esm:
    for i in range(3):
        esm[i] += 1
    if esm[0] > 15:
        esm[0] = 1
    if esm[1] > 28:
        esm[1] = 1
    if esm[2] > 19:
        esm[2] = 1
    year += 1

print(year)