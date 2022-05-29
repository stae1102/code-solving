N, M = map(int, input().split())

d = [[0] * (i + 1) for i in range(N + 1)]

'''
Combination doesn't allow the duplicate and consider the sequence.
nCr = n! // (n-r)! * r!
also,
nCr = n-1Cr-1 + n-1Cr
So you can divide and conquer the combination.
'''

def combination(n, r):
    if r == 0 or r == n:
        d[n][r] = 1
        return 1
    if d[n][r] != 0:
        return d[n][r]
    d[n][r] = combination(n-1, r-1) + combination(n-1, r)
    return d[n][r]

combination(N, M)
print(d[N][M])

'''
Also you can use the bottom-up style dynamic programming.
n, m = map(int, input().split())
r = 1
for i in range(m):
    r = r * (n - i) // (i + 1)
print(r)
'''