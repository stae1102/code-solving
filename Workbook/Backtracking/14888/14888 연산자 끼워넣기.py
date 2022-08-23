import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))

MIN = 1e9
MAX = -1e9

def compute(num, cnt, c):
    global MIN, MAX

    if cnt != 0:
        if c == 0:
            num += arr[cnt]
        elif c == 1:
            num -= arr[cnt]
        elif c == 2:
            num *= arr[cnt]
        else:
            num = int(num / arr[cnt])

    if cnt == n - 1:
        MAX = max(MAX, num)
        MIN = min(MIN, num)
        return

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            compute(num, cnt + 1, i)
            oper[i] += 1

compute(arr[0], 0, 0)

print(MAX)
print(MIN)