import itertools

data = [1, 2, 3, 4]

for x in itertools.permutations(data, 1):
    print(list(x))

print(len(list(itertools.permutations(data, 1))))