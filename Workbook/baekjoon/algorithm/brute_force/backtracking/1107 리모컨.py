import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
if m:
    exc = input().rstrip().split()
else:
    exc = []
btn = []
for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    if i not in exc:
        btn.append(i)

ans = abs(n - 100)

def con(arr, cnt):
    global ans
    if len(arr) > 0:
        ans = min(ans, abs(n - int(arr)) + cnt)
    # print(arr)
    if cnt == len(str(n)) + 1:
        return

    for i in btn:
        if arr and arr[-1] == 0:
            continue
        temp = arr + i
        con(temp, cnt + 1)
        temp = arr

con('', 0)

print(ans)