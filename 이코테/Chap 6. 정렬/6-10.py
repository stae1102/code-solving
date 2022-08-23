n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 내장 라이브러리
# for j in sorted(array, reverse=True):
#     print(j, end=" ")

# 계수 정렬
# count = [0] * (max(array) + 1)
# for i in array:
#     count[i] += 1
# for i in range(len(count) - 1, -1, -1):
#     for j in range(count[i]):
#         print(i, end=' ')