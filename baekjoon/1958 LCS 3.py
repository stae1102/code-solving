import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

l1, l2, l3 = map(len, [word1, word2, word3])

d = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        for k in range(1, l3 + 1):
            if word1[i - 1] == word2[j - 1] == word3[k - 1]:
                d[i][j][k] = d[i - 1][j - 1][k - 1] + 1
            else:
                d[i][j][k] = max(d[i - 1][j][k], d[i]
                                 [j - 1][k], d[i][j][k - 1])

print(d[-1][-1][-1])
