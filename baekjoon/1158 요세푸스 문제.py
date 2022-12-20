n, k = map(int, input().split())

l = [str(i) for i in range(1, n + 1)]
ans = []
idx = 0

while l:
    idx = (idx + k - 1) % len(l)
    ans.append(l.pop(idx))

print("<"+', '.join(ans)+">")