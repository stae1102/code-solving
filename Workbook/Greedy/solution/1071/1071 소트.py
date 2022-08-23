n = int(input())

cnt_sort = [0 for i in range(1002)]

arr = [int(i) for i in input().split()]
for i in range(n):
    cnt_sort[arr[i]] += 1

ans = ''

while True:
    switch = False
    for i in range(1001):
        if cnt_sort[i]:
            switch = True
            if cnt_sort[i + 1]:
                k = -1
                for j in range(i + 2, 1001):
                    if cnt_sort[j]:
                        k = j
                        break
                if k != -1:
                    while cnt_sort[i]:
                        ans += str(i) + ' '
                        cnt_sort[i] -= 1
                    ans += str(k) + ' '
                    cnt_sort[k] -= 1
                    break
                else:
                    ans += str(i + 1) + ' '
                    cnt_sort[i + 1] -= 1
                    break
            else:
                while cnt_sort[i]:
                    ans += str(i) + ' '
                    cnt_sort[i] -= 1
                break
    if switch == False:
        break

print(ans)