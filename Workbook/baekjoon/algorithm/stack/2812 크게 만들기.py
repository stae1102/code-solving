N, K = map(int, input().split())
nums = list(input())

answer = []
cnt = K

for num in nums:
    while answer and answer[-1] < num and cnt > 0:
        answer.pop()
        cnt -= 1
    answer.append(num)

print(''.join(answer[:N-K]))