# highest_number = 0
# highest_score = 0
# for i in range(5):
#     score = sum(list(map(int, input().split())))
#     if highest_score < score:
#         highest_score = score
#         highest_number = i + 1

# print(highest_number, highest_score)

human = [list(map(int, input().split())) for _ in range(5)]
humanScore = [0]*5
score = 0
for i in range(5):
    sum = 0
    for j in range(4):
        sum += human[i][j]
    humanScore[i] = sum
    score = max(score, sum)

for i in range(5):
    if humanScore[i] == score:
        print(i + 1, score)
        break