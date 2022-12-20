# word = input()
# n = len(word)
# map = {}

# for i in range(n):
#     for j in range(n):
#         if word[i:j+1] and word[i:j+1] not in map:
#             map[word[i:j+1]] = 1

# print(len(map))

def sol(s: str) -> int:
    s_len = len(s)
    return sum(len({s[i:i+gap] for i in range(s_len+1-gap)}) for gap in range(1, s_len+1))


print(sol(input()))
