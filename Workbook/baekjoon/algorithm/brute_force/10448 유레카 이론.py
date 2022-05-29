import sys
input = sys.stdin.readline

t = []

def calc():
    i = 1
    while i * (i + 1) // 2 < 1000:
        t.append(i * (i + 1) // 2)
        i += 1

calc()

def triangle(x):
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if t[i] + t[j] + t[k] == x:
                    return 1

for _ in range(int(input())):
    if triangle(int(input())) == 1:
        print(1)
    else:
        print(0)