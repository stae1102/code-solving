from itertools import combinations

a = [[11, 22, 33], [44, 55, 66]]

print(min(map(sum, combinations(a, 2))))