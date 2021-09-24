dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
a = list(input())
count = 0
for i in a:
    for j in dial:
        if i in j: count += dial.index(j) + 3
print(count)
