N = int(input())

csort_a = [0 for i in range(1001)]
csort_b = [0 for i in range(1001)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in A:
    csort_a[i] += 1
for i in B:
    csort_b[i] += 1

ans = 0

for i in range(1, 1001):
    while csort_a[i]:
        switch = False
        for j in range(i - 1, 0, -1):
            if csort_b[j]:
                switch = True
                ans += 2
                csort_a[i] -= 1
                csort_b[j] -= 1
                break
        if switch == False:
            break

for i in range(1, 1001):
    while csort_a[i] and csort_b[i]:
        ans += 1
        csort_a[i] -= 1
        csort_b[i] -= 1

print(ans)