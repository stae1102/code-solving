import sys
input = sys.stdin.readline

w1 = input().strip()
w2 = input().strip()

len_w1, len_w2 = len(w1), len(w2)
d = [0] * len_w2

for i in range(len_w1):
    tmp = 0  # 임시로 받을 변수
    for j in range(len_w2):
        if tmp < d[j]:  # 더 긴 LCS를 발견하였다면, 값을 수정
            tmp = d[j]
        elif w1[i] == w2[j]:
            d[j] = tmp + 1
    print(d)

print(max(d))
