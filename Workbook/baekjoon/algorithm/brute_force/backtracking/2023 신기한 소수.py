N = int(input())

def prime(n):
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True

def solve(arr, cnt):
    if cnt == N:
        print(arr)
        return

    for i in ['1', '3', '7', '9']:
        temp = int(arr + i)
        if not prime(temp): continue
        else: solve(str(temp), cnt + 1)
        temp = arr

for i in ['2', '3', '5', '7']:
    solve(i, 1)