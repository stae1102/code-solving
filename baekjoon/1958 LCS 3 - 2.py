import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

l1, l2, l3 = map(len, [word1, word2, word3])
MIN = min(l1, l2, l3)
d = [0] * l3

for i in range(l1):
    for j in range(l2):
        if word1[i] == word2[j]:
            cnt = 0
            for k in range(l3):
                if cnt < d[k]:
                    cnt = d[k]
                elif word2[j] == word3[k]:
                    d[k] = cnt + 1
                    if d[k] > MIN:
                        d[k] = MIN

print(max(d))
