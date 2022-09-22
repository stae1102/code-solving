import sys
input = sys.stdin.readline

w1 = input().strip()
w2 = input().strip()

len_w1, len_w2 = len(w1), len(w2)
d = [[0, ""] for _ in range(len_w2)]

for i in range(len_w1):
    tmp = 0
    word = ""
    for j in range(len_w2):
        if tmp < d[j][0]:
            tmp = d[j][0]
            word = d[j][1]
        elif w1[i] == w2[j]:
            d[j][0] = tmp + 1  # 개수 추가는 맞음
            d[j][1] = word + w1[i]

print(*max(d), sep="\n")
