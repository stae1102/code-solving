import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
    
rank = [1] * n # 비교군이 없으면 1등이기 때문에
idx = 0 # 인덱스를 늘려가며 검사

for i in l:
    for j in l:
        if (i[0] < j[0] and i[1] < j[1]): # 몸무게와 키가 모두 커야지 그 사람보다 덩치가 작은 것임
            rank[idx] += 1
    idx += 1 # 다음 인덱스로

print(*rank, sep=" ")
