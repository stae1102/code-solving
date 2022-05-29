from itertools import combinations
from re import L

n, m = map(int, input().split())
array = list(input().split())

key = set(['a', 'e', 'i', 'o', 'u'])

array.sort()

for password in combinations(array, n):
    cnt = 0
    for x in password:
        if x in key:
            cnt += 1
    if cnt >= 1 and cnt <= n - 2:
        print(''.join(password))