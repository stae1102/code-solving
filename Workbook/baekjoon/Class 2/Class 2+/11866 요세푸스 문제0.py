n, k = map(int, input().split())

lst = [str(i) for i in range(1, n + 1)]
ans = []
idx = k - 1

while len(ans) != n:
    ans.append(lst[idx])
    lst[idx] = None
    cnt = 0
    if len(ans) == n:
        break
    while cnt < k:
        idx += 1
        if idx > len(lst) - 1:
            idx = 0
        if lst[idx] == None:
            pass
        else:
            cnt += 1

print("<"+', '.join(ans)+">")

##### 시간 복잡도 줄이기 #####

n, k = map(int, input().split())

lst = [str(i) for i in range(1, n + 1)]
ans = []
idx = 0

while lst:
    idx = (idx + k - 1) % len(lst)
    ans.append(lst.pop(idx))

print("<"+', '.join(ans)+">")
