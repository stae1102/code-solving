import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())

arr = input().split()
arr.sort(key=lambda x: int(x))
dict = {}
ans = []
visited = [False] * n

def solve(cnt):
    if cnt == m:
        k = ' '.join(ans)
        if k not in dict:
            dict[k] = 1
            print(k+'\n')
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            solve(cnt + 1)
            visited[i] = False
            ans.pop()

solve(0)