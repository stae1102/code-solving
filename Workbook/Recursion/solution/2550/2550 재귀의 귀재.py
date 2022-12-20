# from sys import stdin
# input = stdin.readline


# def isPalindrom(s, l, r, cnt):
#     if l >= r:
#         return 1, cnt
#     elif (s[l] != s[r]):
#         return 0, cnt
#     else:
#         return isPalindrom(s, l + 1, r - 1, cnt + 1)


# t = int(input())

# for _ in range(t):
#     word = input().rstrip()
#     print(*isPalindrom(word, 0, len(word) - 1, 1))

from sys import stdin
input = stdin.readline


def isPalindrome(word):
    pl, pr = 0, len(word) - 1
    result = 0
    cnt = 0
    while pl < pr:
        cnt += 1
        if word[pl] != word[pr]:
            break
        pl += 1
        pr -= 1
    else:
        cnt += 1
        result = 1
    return result, cnt


t = int(input())
for _ in range(t):
    print(*isPalindrome(input().rstrip()))
