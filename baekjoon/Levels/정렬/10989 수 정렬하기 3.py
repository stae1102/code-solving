import sys
n = int(sys.stdin.readline())

cnt = [0] * 10001

for i in range(n):
    cnt[int(sys.stdin.readline())] += 1
for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    for j in range(cnt[i]):
        print(i, end="\n")
        
"""
카운팅 정렬을 알게 되었고,
메모리를 줄이며 카운팅 정렬하는 방법을 알게 되었다.
"""
