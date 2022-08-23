x = input()
n = len(x)

arr = []
ans = []
visited = [False] * n

def solve(z):
    if z == n:
        k = int(''.join(arr))
        if k > int(x):
            ans.append(k)
            return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(x[i])
            solve(z + 1)
            visited[i] = False
            arr.pop()
solve(0)
ans.sort()

if ans:
    print(ans[0])
else:
    print(0)
