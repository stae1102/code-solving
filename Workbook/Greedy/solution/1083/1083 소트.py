n = int(input())

num = [int(i) for i in input().split()]

s = int(input())

while True:
    tof = False
    for i in range(n):
        idx = i
        cmp = 0
        for j in range(i + 1, n):
            if num[idx] < num[j] and j - i <= s:
                idx = j
                tof = True
                cmp = j - i
        if idx != i:
            tmp = num[idx]
            del num[idx]
            num.insert(i, tmp)
            s -= cmp
            break
    if tof == False:
        break

print(*num)