from sys import stdin, stdout
n = int(stdin.readline())

words = sorted(set(stdin.read().split()))
words.sort(key = lambda x: len(x))

# print(words[0])
# for i in range(1, n):
#     if words[i - 1] == words[i]:
#         continue
#     print(words[i])

print('\n'.join(words))