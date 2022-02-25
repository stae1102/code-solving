import sys
a = int(sys.stdin.readline())
score = 0
for i in range(a):
    b = list(sys.stdin.readline())
    count = 0
    score = 0
    for j in b:
        if j == "O":
            count += 1
            score += count
            continue
        count = 0
    print(score)
