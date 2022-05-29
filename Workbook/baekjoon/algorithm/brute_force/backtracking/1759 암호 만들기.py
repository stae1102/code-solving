l, c = map(int, input().split())
word = input().split()
word.sort()
visited = [False] * c
ans = []

def solve(t, i, j):
    if t == l:
        if j and len(ans) - j > 1:
            print(''.join(ans))
        return
    
    for k in range(i, c):
        if not visited[k]:
            visited[k] = True
            ans.append(word[k])

            if word[k] in 'aeiou':
                solve(t + 1, k + 1, j + 1)
            else:
                solve(t + 1, k + 1, j)
            
            visited[k] = False
            ans.pop()

solve(0, 0, 0)

# import sys
# l, c = map(int, sys.stdin.readline().split())
# arr = sys.stdin.readline().split()
# arr.sort()
# visit = [0] * c
# word = []

# def back(k, next, v):
#     if k == l:
#         if v and len(word) - v > 1:
#             print(''.join(word))
#         return

#     for i in range(next, c):
#         if visit[i] == 0:
#             visit[i] = 1
#             word.append(arr[i])

#             if arr[i] in 'aeiou':
#                 back(k + 1, i + 1, v + 1)
#             else:
#                 back(k + 1, i + 1, v)

#             visit[i] = 0
#             word.pop()

# back(0, 0, 0)