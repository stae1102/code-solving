import itertools

data = [1, 2, 3, 4]

for x in itertools.combinations(data, 2):
    print(list(x))